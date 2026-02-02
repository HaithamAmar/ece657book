# Test Matrix (Minimum Devices/Readers)

Goal: prevent reader-specific failures (missing figures, clipped math, broken navigation) before publishing.
All paths are relative to the repo root `ece657Book/`.

## Required (every release candidate)

### Apple EPUB (`epub_builder/dist/ece657_ebook_apple.epub`)
- Apple Books (macOS)
  - Verify cover thumbnail in library
  - Verify TOC works
  - Verify a few dense-math pages render and can scroll if needed
  - Verify several figure-heavy chapters
- Apple Books (iOS/iPadOS) — if available
  - Spot-check same items (small screen stress test)

### Kindle EPUB (`epub_builder/dist/ece657_ebook_kindle.epub`)
- Kindle Previewer (desktop)
  - Verify cover thumbnail
  - Jump to several figures (including the largest diagrams)
  - Verify at least one wide table and one multi-line derivation
- Physical Kindle device (strongly recommended before paid release)
  - Same checks as Kindle Previewer; physical devices can differ

## Suggested “worst-case” content to spot-check

Pick representative pages each time (do not rely on memory):
- A long derivation / multi-line equation
- A `cases` environment
- A wide or dense table
- A figure with small labels (axes/ticks)
- A callout box (tcolorbox-derived)
- An appendix cross-reference (Appendix A/B/C)

## Acceptance criteria (definition of done)

- No missing figures (no blank figure areas; captions match).
- No clipped display math (horizontal scroll acceptable in Apple; Kindle must not shrink to illegibility).
- Tables readable without extreme zoom; if scroll is used, it is discoverable and not broken.
- TOC/navigation works and headings are consistent (no random unnumbered headings in the middle of numbered sections).

