// Kartvizit yüzlerini baskı PDF'i (91×61 / 61×91 mm, taşmalı) + 300 dpi PNG olarak üretir.
// Çalıştır: NODE_PATH=C:\Users\Admin\epot-muhendislik\tools\node_modules node build.cjs
const puppeteer = require('puppeteer-core');
const path = require('path');
const { pathToFileURL } = require('url');

const OUT = path.resolve(__dirname, '..');
const PX_PER_MM = 96 / 25.4;
const DPR = 300 / 96; // 300 dpi
const faces = ['v1-on','v1-arka','v2-on','v2-arka','v3-on','v3-arka','v4-on','v4-arka'];
const dikey = new Set(['v2-on','v2-arka']);

(async () => {
  const browser = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', args: ['--allow-file-access-from-files'] });
  const page = await browser.newPage();
  const errors = [];
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('requestfailed', r => errors.push('FAILED ' + r.url()));
  for (const f of faces) {
    const [wmm, hmm] = dikey.has(f) ? [61, 91] : [91, 61];
    const w = wmm * PX_PER_MM, h = hmm * PX_PER_MM;
    await page.setViewport({ width: Math.ceil(w), height: Math.ceil(h), deviceScaleFactor: DPR });
    await page.goto(pathToFileURL(path.join(__dirname, f + '.html')).href, { waitUntil: 'networkidle0' });
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({ path: path.join(OUT, f + '.pdf'), width: wmm + 'mm', height: hmm + 'mm', printBackground: true, preferCSSPageSize: true, pageRanges: '1' });
    await page.screenshot({ path: path.join(OUT, f + '.png'), clip: { x: 0, y: 0, width: w, height: h } });
    const fonts = await page.evaluate(() => [...document.fonts].filter(x => x.status === 'loaded').map(x => x.family + ' ' + x.weight));
    console.log(f, wmm + 'x' + hmm, 'fonts:', [...new Set(fonts)].join(', '));
  }
  if (errors.length) console.log('HATALAR:\n' + errors.join('\n'));
  await browser.close();
})();
