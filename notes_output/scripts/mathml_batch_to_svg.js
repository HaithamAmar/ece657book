#!/usr/bin/env node
/* Convert a batch of MathML strings to SVG using MathJax. */

const fs = require('fs');
const path = require('path');

let mathjax;
try {
  mathjax = require('mathjax-full/js/mathjax.js');
} catch (err) {
  console.error('mathjax-full is required. Run: npm install mathjax-full');
  throw err;
}

const { MathML } = require('mathjax-full/js/input/mathml.js');
const { SVG } = require('mathjax-full/js/output/svg.js');
const { liteAdaptor } = require('mathjax-full/js/adaptors/liteAdaptor.js');
const { RegisterHTMLHandler } = require('mathjax-full/js/handlers/html.js');

const args = process.argv.slice(2);
if (args.length < 2) {
  console.error('Usage: mathml_batch_to_svg.js <input.json> <output_dir>');
  process.exit(2);
}

const inputPath = path.resolve(args[0]);
const outDir = path.resolve(args[1]);
if (!fs.existsSync(inputPath)) {
  console.error(`Input JSON not found: ${inputPath}`);
  process.exit(2);
}
if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

const payload = JSON.parse(fs.readFileSync(inputPath, 'utf8'));
if (!Array.isArray(payload)) {
  console.error('Input JSON must be an array of {id, mathml} objects.');
  process.exit(2);
}

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);

const mathml = new MathML();
const svg = new SVG({ fontCache: 'local' });
const html = mathjax.mathjax.document('', { InputJax: mathml, OutputJax: svg });

function sanitizeMathML(input) {
  if (!input) return input;
  // TeX4ht injects XML comments (e.g., FUNCTION APPLICATION) and empty label
  // markers inside MathML; these can trigger MathJax parser failures.
  let out = input.replace(/<!--[\s\S]*?-->/g, '');
  out = out.replace(/<mstyle\b[^>]*\bclass=['"]label['"][^>]*>\s*<\/mstyle>/gi, '');
  // TeX4ht sometimes emits `arg min` / `arg max` using an `munder` base that
  // can trigger MathJax failures. Rewrite into a simpler, valid MathML form.
  out = out.replace(
    /<munder\b[^>]*>\s*<mrow>\s*<mstyle\s+class=['"]qopname['"]>\s*arg\s*(<mspace\b[^>]*>\s*<\/mspace>)\s*(min|max)\s*<\/mstyle>\s*<mo\b[^>]*>[\s\S]*?<\/mo>\s*<\/mrow>\s*<mrow>\s*([\s\S]*?)\s*<\/mrow>\s*<\/munder>/gi,
    (_m, _mspace, op, sub) => `<munder><mi>arg${op}</mi><mrow>${sub}</mrow></munder>`
  );
  // TeX4ht sometimes emits operator names as raw text nodes inside <mstyle>,
  // which MathJax's MathML parser rejects. Rewrite the known pattern for
  // `arg min` / `arg max` into explicit token elements.
  out = out.replace(
    /<mstyle\s+class=['"]qopname['"]>\s*arg\s*(<mspace\b[^>]*>\s*<\/mspace>)\s*(min|max)\s*<\/mstyle>/gi,
    (_m, mspace, op) => `<mrow><mi>arg</mi>${mspace}<mi>${op}</mi></mrow>`
  );
  // MathJax's MathML input can choke on TeX4ht's class-heavy markup.
  out = out.replace(/\s+class=['"][^'"]*['"]/gi, '');
  // TeX4ht inserts a separate mo token for U+2061 FUNCTION APPLICATION.
  // Drop it; MathJax can infer function application without this token.
  out = out.replace(/<mo\b[^>]*>\s*⁡\s*<\/mo>/gi, '');
  return out;
}

const failures = [];
for (const entry of payload) {
  if (!entry || !entry.id || !entry.mathml) {
    continue;
  }
  try {
    const display = entry.display === undefined ? true : Boolean(entry.display);
    const node = html.convert(sanitizeMathML(entry.mathml), { display });
    const raw = adaptor.outerHTML(node);
    // MathJax wraps SVG output in an <mjx-container>. For EPUB image assets we
    // want a standalone <svg> document.
    const m = raw.match(/<svg[\s\S]*<\/svg>/i);
    const svgText = m ? m[0] : raw;
    const outPath = path.join(outDir, `${entry.id}.svg`);
    fs.writeFileSync(outPath, svgText, 'utf8');
  } catch (err) {
    failures.push({ id: entry.id, message: String(err.message || err) });
  }
}

if (failures.length) {
  const failurePath = path.join(outDir, '_mathml_failures.json');
  fs.writeFileSync(failurePath, JSON.stringify(failures, null, 2), 'utf8');
}
