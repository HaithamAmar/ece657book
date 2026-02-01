#!/usr/bin/env python3
"""Extract board-writing content from lecture frames using OpenAI vision."""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image
from scipy.ndimage import sobel

try:
    from openai import OpenAI
except Exception as exc:  # pragma: no cover
    raise SystemExit(f"OpenAI SDK not available: {exc}")


def _load_api_key() -> str:
    key = os.getenv("OPENAI_API_KEY")
    if key:
        return key
    # Fallback to .env
    env_path = Path(".env")
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("OPENAI_API_KEY="):
                return line.split("=", 1)[1].strip()
    raise SystemExit("OPENAI_API_KEY not set.")


def _edge_score(image_path: Path) -> float:
    img = Image.open(image_path).convert("L")
    arr = np.asarray(img, dtype=np.float32)
    dx = sobel(arr, axis=0, mode="reflect")
    dy = sobel(arr, axis=1, mode="reflect")
    mag = np.hypot(dx, dy)
    return float(np.mean(mag))


def _pick_frames(window_dir: Path, k: int = 2) -> list[Path]:
    frames = sorted(window_dir.glob("frame_*.jpg"))
    if not frames:
        return []
    scores = [(fp, _edge_score(fp)) for fp in frames]
    scores.sort(key=lambda x: x[1], reverse=True)
    picked = [fp for fp, _ in scores[:k]]
    return picked


def _encode_image(path: Path) -> str:
    data = path.read_bytes()
    return base64.b64encode(data).decode("utf-8")


def _window_timestamp(window_name: str) -> str:
    # window_02_1240s -> 00:20:40
    m = re.search(r"_(\d+)s$", window_name)
    if not m:
        return "unknown"
    t = int(m.group(1))
    hh = t // 3600
    mm = (t % 3600) // 60
    ss = t % 60
    return f"{hh:02d}:{mm:02d}:{ss:02d}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0, help="Limit number of windows to process.")
    parser.add_argument("--start", type=int, default=0, help="Skip first N windows.")
    args = parser.parse_args()

    api_key = _load_api_key()
    client = OpenAI(api_key=api_key)

    base = Path("notes_output/artifacts/lecture_source/lecture8part2")
    frames_root = base / "frames_windows"
    out_json = base / "vision_notes.json"
    out_md = base / "vision_notes.md"

    results: list[dict[str, Any]] = []

    windows = sorted(frames_root.glob("window_*"))
    if args.start:
        windows = windows[args.start :]
    if args.limit and args.limit > 0:
        windows = windows[: args.limit]

    for window_dir in windows:
        picked = _pick_frames(window_dir, k=2)
        if not picked:
            continue
        images = []
        for fp in picked:
            images.append({
                "type": "input_image",
                "image_url": f"data:image/jpeg;base64,{_encode_image(fp)}",
            })
        ts = _window_timestamp(window_dir.name)

        prompt = (
            "You are reading lecture board screenshots. Extract ALL legible content. "
            "Return JSON with keys: summary, equations (list of strings), diagrams (list of strings), "
            "notations (list), and notes (list). If unreadable, say so explicitly." 
        )

        response = client.responses.create(
            model="gpt-4o",
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": f"Window {window_dir.name} at ~{ts}"},
                        {"type": "input_text", "text": prompt},
                        *images,
                    ],
                }
            ],
        )

        text = response.output_text
        results.append(
            {
                "window": window_dir.name,
                "timestamp": ts,
                "frames": [p.name for p in picked],
                "raw": text,
            }
        )

    out_json.write_text(json.dumps(results, indent=2), encoding="utf-8")

    # Simple markdown render
    md_lines = ["# Lecture 8 Part 2 – Vision Notes", ""]
    for entry in results:
        md_lines.append(f"## {entry['window']} ({entry['timestamp']})")
        md_lines.append(f"Frames: {', '.join(entry['frames'])}")
        md_lines.append("")
        md_lines.append("```json")
        md_lines.append(entry["raw"].strip())
        md_lines.append("```")
        md_lines.append("")

    out_md.write_text("\n".join(md_lines), encoding="utf-8")
    print(out_json)
    print(out_md)


if __name__ == "__main__":
    main()
