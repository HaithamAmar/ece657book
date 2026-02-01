# EPUB editorial layout audit
- EPUB: `epub_builder/dist/ece657_ebook_apple.epub`
- XHTML files scanned: 29
- Issues found: 0

## What this audit checks
- Horizontal overflow candidates (`math`, `pre`, `code`, `table`, `img`, `svg`) whose bounding box extends beyond the viewport.

## Issues
- None detected by the automated layout scanner.

## Suggested global fixes
- Prefer block math for long derivations (promote `\(\displaystyle ...\)` to `\[...\]`).
- Keep `math[display="block"]` horizontally scrollable as a safety net.
- Avoid oversized tables; ensure table CSS sets reasonable `min-width` and preserves readability.

