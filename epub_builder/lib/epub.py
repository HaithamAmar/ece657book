from __future__ import annotations

import subprocess
import shutil
from pathlib import Path


def postprocess_epub_minimal(epub_path: Path) -> None:
    # Keep this as a no-op for now.
    #
    # We prefer emitting stable HTML/CSS directly from Pandoc rather than
    # unpacking/repacking EPUBs (slow and can be flaky across platforms).
    if not epub_path.exists():
        raise FileNotFoundError(epub_path)
    return


def run_epubcheck(epub_path: Path, *, out_dir: Path) -> None:
    epubcheck = shutil.which("epubcheck")
    if epubcheck is None:
        return
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / f"{epub_path.stem}.epubcheck.txt"
    with log_path.open("w", encoding="utf-8") as f:
        subprocess.run([epubcheck, str(epub_path)], stdout=f, stderr=subprocess.STDOUT, check=False)
