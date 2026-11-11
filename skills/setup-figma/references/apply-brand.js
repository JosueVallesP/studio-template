// apply-brand.js: put a person's brand on their copy of the visual kit.
// Run with the Figma tool (use_figma) on the person's file. Fill BRAND first, from
// canon/visual/design-system.md when it exists, otherwise canon/visual/brand-assets.md.
// Leave a value null when the person didn't give it: the script derives it or keeps the neutral one.
// It changes the "Brand" mode and the text styles only. The "Neutral" mode is never touched.

const BRAND = {
  name: null,                         // their name for the footers, e.g. "Ana Ruiz"
  colors: {
    paper: null,                      // background, e.g. "#FBF8F2"
    ink: null,                        // text and filled marks
    line: null,                       // lines and strokes (defaults to ink)
    muted: null,                      // captions and greyed marks (defaults to a mix of ink and paper)
    accent: null,                     // the one thing to look at: their strongest brand color
    'accent-2': null,                 // a second accent, only if the brand has one (defaults to accent)
    panel: null,                      // cells and panels (defaults to a light tint of ink on paper)
  },
  fonts: { heading: null, body: null }, // family names as Figma lists them, e.g. "Playfair Display"
};

const hex = h => ({ r: parseInt(h.slice(1, 3), 16) / 255, g: parseInt(h.slice(3, 5), 16) / 255, b: parseInt(h.slice(5, 7), 16) / 255, a: 1 });
const mix = (a, b, t) => ({ r: a.r + (b.r - a.r) * t, g: a.g + (b.g - a.g) * t, b: a.b + (b.b - a.b) * t, a: 1 });
const lum = c => { const f = x => (x <= 0.03928 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4)); return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b); };
const contrast = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((m, n) => n - m); return (x + 0.05) / (y + 0.05); };

const col = (await figma.variables.getLocalVariableCollectionsAsync()).find(c => c.name === 'Style');
if (!col) throw new Error('No "Style" collection: this is not a copy of the template library.');
const brandMode = col.modes.find(m => m.name === 'Brand');
const neutralMode = col.modes.find(m => m.name === 'Neutral');
const vars = {};
for (const id of col.variableIds) { const v = await figma.variables.getVariableByIdAsync(id); vars[v.name] = v; }
const neutral = n => vars['color/' + n].valuesByMode[neutralMode.modeId];

const c = {};
for (const k of ['paper', 'ink', 'accent']) c[k] = BRAND.colors[k] ? hex(BRAND.colors[k]) : neutral(k);
c.line = BRAND.colors.line ? hex(BRAND.colors.line) : c.ink;
c.muted = BRAND.colors.muted ? hex(BRAND.colors.muted) : mix(c.ink, c.paper, 0.45);
c['accent-2'] = BRAND.colors['accent-2'] ? hex(BRAND.colors['accent-2']) : c.accent;
c.panel = BRAND.colors.panel ? hex(BRAND.colors.panel) : mix(c.paper, c.ink, 0.06);
for (const [k, v] of Object.entries(c)) vars['color/' + k].setValueForMode(brandMode.modeId, v);

const report = { colors: {}, warnings: [], fonts: {}, pages: [], footers: 0 };
for (const [k, v] of Object.entries(c)) report.colors[k] = '#' + [v.r, v.g, v.b].map(x => Math.round(x * 255).toString(16).padStart(2, '0')).join('').toUpperCase();
const ip = contrast(c.ink, c.paper), ap = contrast(c.accent, c.paper);
if (ip < 4.5) report.warnings.push(`ink on paper is ${ip.toFixed(1)}:1; text needs 4.5:1 to read at feed size`);
if (ap < 3) report.warnings.push(`accent on paper is ${ap.toFixed(1)}:1; marks in the accent need 3:1 to be seen`);

// Fonts: heading font on Display, Headline, Subhead; body font on the rest. Nearest weight wins.
const W = { thin: 100, extralight: 200, 'extra light': 200, light: 300, regular: 400, book: 400, normal: 400, medium: 500, semibold: 600, 'semi bold': 600, demibold: 600, bold: 700, extrabold: 800, 'extra bold': 800, black: 900, heavy: 900 };
const weightOf = s => { const k = s.toLowerCase().replace(/italic/g, '').trim(); return W[k] ?? 400; };
const available = await figma.listAvailableFontsAsync();
const stylesOf = fam => available.filter(f => f.fontName.family === fam && !/italic/i.test(f.fontName.style)).map(f => f.fontName.style);
const ROLE = { Display: 'heading', Headline: 'heading', Subhead: 'heading', Body: 'body', Label: 'body', 'Small label': 'body', Caption: 'body' };
for (const ts of await figma.getLocalTextStylesAsync()) {
  const short = ts.name.replace('Studio/', ''); const fam = BRAND.fonts[ROLE[short]];
  if (!fam) continue;
  const styles = stylesOf(fam);
  if (!styles.length) { report.warnings.push(`font "${fam}" isn't available in Figma; ${short} keeps ${ts.fontName.family}`); continue; }
  const want = weightOf(ts.fontName.style);
  const pick = styles.slice().sort((a, b) => Math.abs(weightOf(a) - want) - Math.abs(weightOf(b) - want))[0];
  await figma.loadFontAsync({ family: fam, style: pick });
  ts.fontName = { family: fam, style: pick };
  report.fonts[short] = `${fam} ${pick}`;
}

// Show the Brand mode on every page with pictures on it. The Start here page stays neutral.
for (const p of figma.root.children) {
  if (['Kit', 'Moves (examples)', 'Plays', 'Carousel', 'Field guide and plate', 'LinkedIn placements', 'Substack placements', 'Brand'].includes(p.name)) { p.setExplicitVariableModeForCollection(col, brandMode.modeId); report.pages.push(p.name); }
}
report.next = 'Footers: run the footer step on each template page (one page per call) when BRAND.name is set.';
return report;
