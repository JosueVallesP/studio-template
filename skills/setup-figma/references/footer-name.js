// footer-name.js: put the person's name wherever the kit says "Your name" on one page. Run once per page
// (Figma loads one page per call): Moves (examples), Carousel, Field guide and plate, LinkedIn placements,
// Substack placements. Set PAGE_NAME and NAME.
const PAGE_NAME = 'Moves (examples)';
const NAME = null; // e.g. "Ana Ruiz"
if (!NAME) return { skipped: 'no name' };
const page = figma.root.children.find(p => p.name === PAGE_NAME);
await figma.setCurrentPageAsync(page);
let n = 0;
for (const t of page.findAllWithCriteria({ types: ['TEXT'] })) {
  if (!/Your name|YOUR NAME/.test(t.characters)) continue;
  await Promise.all(t.getStyledTextSegments(['fontName']).map(s => figma.loadFontAsync(s.fontName)));
  t.characters = t.characters.replace(/Your name( or mark)?/g, NAME).replace(/YOUR NAME/g, NAME.toUpperCase());
  n++;
}
return { page: PAGE_NAME, replaced: n };
