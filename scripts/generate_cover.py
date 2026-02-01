"""
Generate a cover image via the OpenAI Images API.

Usage:
  1) Ensure .env contains OPENAI_API_KEY
  2) pip install openai python-dotenv
  3) python scripts/generate_cover.py
Output:
  notes_output/KDP print specs/cover.png
"""

import base64
import os
from pathlib import Path
from textwrap import dedent

from dotenv import load_dotenv
from openai import OpenAI


def main() -> None:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY not set in .env")

    client = OpenAI(api_key=api_key)

    prompt = dedent(
        """
        A clean, modern book cover for a graduate technical companion.
        Title: "Modern Intelligent Systems"
        Subtitle: "Neural Networks, Fuzzy Logic, and Evolutionary Optimization"
        Style: minimal, geometric shapes, cool palette, scientific/technical feel,
        no people, high contrast, suitable for print. Include subtle network/graph motifs.
        """
    )

    print("Requesting image from OpenAI...")
    resp = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        # Use a supported size; 1536x1024 is wide and easy to crop to 7x10
        size="1536x1024",
        n=1,
    )
    img_b64 = resp.data[0].b64_json

    out_path = Path("notes_output/KDP print specs/cover.png")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(base64.b64decode(img_b64))
    print(f"Saved cover to {out_path.resolve()}")
    print("Note: crop/resize to 7x10 in at 300 dpi for print if needed.")


if __name__ == "__main__":
    main()