#!/usr/bin/env python3
"""Generate blog_posts/posts.json from markdown files in blog_posts/."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOG_DIR = ROOT / "blog_posts"
MANIFEST_PATH = BLOG_DIR / "posts.json"


def load_posts() -> list[dict[str, str]]:
    posts: list[dict[str, str]] = []

    for path in sorted(BLOG_DIR.glob("*.md")):
        posts.append(
            {
                "filename": path.name,
                "markdown": path.read_text(encoding="utf-8"),
            }
        )

    return posts


def main() -> None:
    if not BLOG_DIR.exists():
        raise SystemExit(f"blog directory not found: {BLOG_DIR}")

    posts = load_posts()
    MANIFEST_PATH.write_text(
        json.dumps(posts, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {MANIFEST_PATH} with {len(posts)} post(s)")


if __name__ == "__main__":
    main()
