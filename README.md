# MiaMaths Blog Content

This repository stores markdown blog content for the MiaMaths app.
The app loads these files from GitHub at runtime, so publishing does not require redeploying the app.

## Structure

- `blog_posts/*.md`
- `blog_posts/posts.json` (auto-generated manifest for runtime loading)

Each post filename should be:

- `YYYY-MM-DD-your-slug.md`

Front matter is optional, but recommended:

```markdown
---
title: Your title
summary: One sentence summary shown on the blog list
published_on: 2026-02-24
slug: your-slug
---

Your markdown content here.
```

If front matter is omitted:

- `slug` is derived from filename
- `published_on` is derived from filename date
- `title` is derived from slug
- `summary` is derived from the first paragraph

## Publish workflow

1. Add or edit files under `blog_posts/`.
2. Commit and push to `main`.
3. GitHub Actions regenerates `blog_posts/posts.json` automatically.
4. Wait for app cache TTL (`BLOG_CACHE_TTL_MS`, default 5 minutes) or trigger app restart.

## GitHub Pages

Enable GitHub Pages for this repository (branch `main`, folder `/ (root)`).
The app can then fetch the manifest from:

- `https://zimakki.github.io/mia-maths-blog-content/blog_posts/posts.json`

Manifest entries contain:

- `filename` (source markdown filename)
- `markdown` (full markdown body with optional front matter)

## App configuration

In the app deployment, set:

- `BLOG_SOURCE=github`
- `BLOG_GITHUB_REPO=zimakki/mia-maths-blog-content`
- `BLOG_GITHUB_BRANCH=main`
- `BLOG_GITHUB_PATH=blog_posts`
- `BLOG_GITHUB_PAGES_BASE_URL=https://zimakki.github.io/mia-maths-blog-content`
- `BLOG_GITHUB_PAGES_MANIFEST=posts.json`
- Optional for private repo or higher rate limits: `BLOG_GITHUB_TOKEN`
