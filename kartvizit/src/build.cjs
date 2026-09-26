// Tur 2: baskı PDF'leri (taşmalı), katman PDF'leri, 300 dpi düz PNG'ler ve mockup PNG'leri.
// Çalıştır: NODE_PATH=C:\Users\Admin\epot-muhendislik\tools\node_modules node build.cjs
const puppeteer = require('puppeteer-core');
const path = require('path');
const { pathToFileURL } = require('url');

const OUT = path.resolve(__dirname, '..');
const PX_PER_MM = 96 / 25.4;
const faces = {
  'A-on':   { katman: ['kabartma'] },
  'A-arka': { katman: [] },
  'B-on':   { katman: ['folyo'] },
  'B-arka': { katman: ['folyo', 'beyaz', 'murekkep'] },
  'C-on':   { katman: ['folyo', 'kabartma'], dikey: true },
  'C-arka': { katman: ['beyaz', 'murekkep'], dikey: true },
  'D1-on': { katman: [] }, 'D1-arka': { katman: [] },
  'D2-on': { katman: [] }, 'D2-arka': { katman: [] },
};
const url = (f, q = '') => pathToFileURL(path.join(__dirname, f)).href + q;

(async () => {
  const browser = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const page = await browser.newPage();
  const errors = [];
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', e => errors.push(e.message));
  page.on('requestfailed', r => errors.push('FAILED ' + r.url()));
  const load = async u => { await page.goto(u, { waitUntil: 'networkidle0' }); await page.evaluate(() => document.fonts.ready); };

  const yalniz = (process.argv.find(a => a.startsWith('--yalniz=')) || '').split('=')[1];
  for (const [f, o] of Object.entries(faces)) {
    if (yalniz && !f.startsWith(yalniz)) continue;
    const [wmm, hmm] = o.dikey ? [61, 91] : [91, 61];
    const w = wmm * PX_PER_MM, h = hmm * PX_PER_MM;
    const pdf = file => page.pdf({ path: path.join(OUT, file), width: wmm + 'mm', height: hmm + 'mm', printBackground: true, preferCSSPageSize: true, pageRanges: '1' });
    await page.setViewport({ width: Math.ceil(w), height: Math.ceil(h), deviceScaleFactor: 300 / 96 });
    await load(url(f + '.html'));
    await pdf(f + '.pdf');
    await page.screenshot({ path: path.join(OUT, f + '.png'), clip: { x: 0, y: 0, width: w, height: h } });
    for (const k of o.katman) { await load(url(f + '.html', '?katman=' + k)); await pdf(`${f}-${k}.pdf`); }
    console.log(f, wmm + 'x' + hmm, 'katman:', o.katman.join(',') || '-');
  }

  if (process.argv.includes('--mockup')) {
    for (const v of (yalniz ? [yalniz + '1'] : ['A', 'B', 'C', 'D1'])) {
      await page.setViewport({ width: 1000, height: 640, deviceScaleFactor: 2 });
      await load(url('mockup.html', '?v=' + v));
      for (const fr of page.frames().slice(1)) await fr.evaluate(() => document.fonts.ready);
      await new Promise(r => setTimeout(r, 300));
      await page.screenshot({ path: path.join(OUT, `mockup-${v}.png`) });
      console.log('mockup', v);
    }
  }
  if (errors.length) console.log('HATALAR:\n' + errors.join('\n'));
  await browser.close();
})();
