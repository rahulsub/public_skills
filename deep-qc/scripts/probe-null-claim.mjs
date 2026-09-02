#!/usr/bin/env node
/**
 * probe-null-claim.mjs — prove (or disprove) "nothing happened".
 *
 * Never file a null finding from a screenshot at rest. This arms a
 * document-level MutationObserver BEFORE the action, captures the full
 * viewport at several offsets after it, and enumerates live regions and
 * overlays — because feedback frequently renders on a different surface than
 * the one you are driving.
 *
 *   node probe-null-claim.mjs --url <url> --click "<selector or text>" \
 *        [--out ./probe] [--wait 5000] [--width 1280] [--height 800]
 *
 * Requires playwright in the working project (npx playwright install chromium).
 */
import { chromium } from "playwright";
import fs from "node:fs";
import path from "node:path";

const arg = (k, d) => { const i = process.argv.indexOf(`--${k}`); return i > -1 ? process.argv[i + 1] : d; };
const url = arg("url"), target = arg("click");
const out = arg("out", "./probe"), waitMs = +arg("wait", 5000);
const width = +arg("width", 1280), height = +arg("height", 800);
if (!url || !target) { console.error("need --url and --click"); process.exit(2); }
fs.mkdirSync(out, { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width, height } });
await page.goto(url, { waitUntil: "networkidle" });

// Arm the observer BEFORE acting — this is the whole point.
await page.evaluate(() => {
  window.__mut = [];
  window.__t0 = performance.now();
  new MutationObserver(rs => {
    for (const r of rs) {
      const d = Math.round(performance.now() - window.__t0);
      const desc = n => n && n.nodeType === 1
        ? `<${n.tagName.toLowerCase()}${n.className ? "." + String(n.className).slice(0, 60) : ""}> ${(n.textContent || "").trim().slice(0, 120)}`
        : String(n && n.textContent || "").trim().slice(0, 120);
      for (const n of r.addedNodes) window.__mut.push({ t: d, kind: "added", node: desc(n) });
      for (const n of r.removedNodes) window.__mut.push({ t: d, kind: "removed", node: desc(n) });
      if (r.type === "attributes") window.__mut.push({ t: d, kind: "attr", attr: r.attributeName, node: desc(r.target) });
    }
  }).observe(document.body, { subtree: true, childList: true, attributes: true, characterData: true });
});

const el = target.startsWith("text=") || target.startsWith("//")
  ? page.locator(target) : page.locator(target).first();
const box = await el.boundingBox().catch(() => null);
await page.screenshot({ path: path.join(out, "00-before.png"), fullPage: false });
await el.click({ timeout: 5000 }).catch(e => console.error("click failed:", e.message));

for (const ms of [150, 400, 1000]) {
  await page.waitForTimeout(ms === 150 ? 150 : ms === 400 ? 250 : 600);
  await page.screenshot({ path: path.join(out, `+${ms}ms.png`), fullPage: false });
}
await page.waitForTimeout(Math.max(0, waitMs - 1000));
await page.screenshot({ path: path.join(out, "99-settled.png"), fullPage: false });

const report = await page.evaluate(() => {
  const vis = el => { const s = getComputedStyle(el); const r = el.getBoundingClientRect();
    return s.display !== "none" && s.visibility !== "hidden" && +s.opacity > 0.05 && r.width > 0 && r.height > 0; };
  const grab = sel => [...document.querySelectorAll(sel)].filter(vis).map(e => ({
    sel, text: (e.textContent || "").trim().slice(0, 200),
    at: (({ x, y, width, height }) => ({ x: Math.round(x), y: Math.round(y), w: Math.round(width), h: Math.round(height) }))(e.getBoundingClientRect()),
  }));
  return {
    mutations: window.__mut.length,
    firstMutations: window.__mut.slice(0, 40),
    liveRegions: [...grab("[aria-live]"), ...grab("[role=status]"), ...grab("[role=alert]"), ...grab("[role=tooltip]")],
  };
});
report.clickTarget = box ? { x: Math.round(box.x), y: Math.round(box.y), w: Math.round(box.width), h: Math.round(box.height) } : null;
fs.writeFileSync(path.join(out, "report.json"), JSON.stringify(report, null, 2));

console.log(`mutations: ${report.mutations}`);
console.log(`live/overlay regions visible after action: ${report.liveRegions.length}`);
for (const r of report.liveRegions) console.log(`  ${r.sel} @(${r.at.x},${r.at.y}) "${r.text.slice(0, 90)}"`);
console.log(report.mutations === 0 && report.liveRegions.length === 0
  ? "\nVERDICT: no DOM response detected — a null claim is defensible (state it with these numbers)."
  : "\nVERDICT: the page DID respond. Do NOT file 'nothing happened'; inspect the captures — feedback may render away from your click.");
await browser.close();
