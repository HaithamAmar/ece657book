# EPUB Tables (Policy + Audit)

This file captures (1) the current table policy for reflowable EPUB and (2) the latest automated table audit output.

## Policy (EPUB-first)

### Default rendering rule
- Every HTML `<table>` in the EPUB must be wrapped in a horizontal scroll container (`<div class="table-wrap">`) so tables never shrink to microscopic text on narrow screens.

### When to redesign (source-level)
Use this decision tree for any table that still feels bad in Apple Books / Kindle Previewer even with scroll:
1. **> 4 columns** or long text columns → split into 2 smaller tables.
2. “Checklist / steps / bullets” disguised as a table → convert to list or callout box.
3. If the table is purely schematic (small number of entries) → rewrite as prose.
4. If the table is a dense reference and must remain as-is → keep as table + scroll; verify on Kindle.

### Captions and consistency
- Captions should read like tables. Avoid `Schematic:` by default; use it only when the table could be mistaken for an empirical result or a measured/to-scale artifact. Prefer starting with a concrete noun phrase (e.g., "Handling class imbalance..." / "Transformation toolkit...") and, when needed, use wording like "Illustrative" to signal non-empirical content.
- Keep table text short; push long explanations into surrounding prose.

## How to re-run the audit

```bash
stamp=$(date +%Y%m%d_%H%M%S)
python3 epub_builder/build.py --variant apple --clean
python3 epub_builder/scripts/audit_epub_tables.py \
  --epub epub_builder/dist/ece657_ebook_apple.epub \
  --out-json epub_builder/artifacts/qc/epub_table_audit_${stamp}.json \
  --out-md notes_output/EPUB_TABLES_AUDIT.md \
  --flag-cols 5
```

Then open:
- `notes_output/EPUB_TABLES_AUDIT.md`
