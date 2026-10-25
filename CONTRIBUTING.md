# Contributing

## Setup and Commands

Install Make and Pandoc with Lua filter support. The local preview server uses `$HOME/Applications/appvenv/bin/python`. If that environment does not exist, create it with an installed Python 3:

```sh
python3 -m venv "$HOME/Applications/appvenv"
```

No Ruby or Jekyll setup is required.

Run commands from the repository root:

| Command | Purpose |
| --- | --- |
| `make build` | Render changed Markdown pages and copy assets and `CNAME` into `docs/`. |
| `make check` | Build and check `docs/index.html`, `docs/404.html`, and that `docs/CNAME` matches the root file. |
| `make serve` | Build and serve `docs/` at `http://localhost:8000`; stop with Ctrl-C. |
| `make rebuild` | Remove `docs/` and regenerate the entire site. |
| `make clean` | Remove the generated `docs/` directory. |

Use `PANDOC=/path/to/pandoc make build` to select a different Pandoc binary. `PYTHON=/path/to/python make serve` explicitly overrides the preview interpreter. The server listens on `127.0.0.1:8000`; use `make serve PORT=8001` if that port is occupied. It does not rebuild automatically; run `make build` after further edits.

## Tool and Code Defaults

The [Tools and Coding rules in AGENTS.md](AGENTS.md#tools-and-coding) apply to contributors and agents: use POSIX `sh` and standard utilities for automation, the explicit `appvenv` interpreter for Python, and C11 or later for new compiled helpers. Follow the STB implementation-macro pattern, explicit struct-based arrays, and arena allocation. Keep changes focused, review generated code, and verify behavior with the project's documented checks.

The [computing guide](content/computing.md) explains the full environment, SSH, editor setup, memory conventions, and agent workflow.

Keep scratch files and temporary tool state in the ignored repository-local `build/`, `tmp/`, or `work/` directories. Make targets create `tmp/` and export its absolute path as `TMPDIR`. Configure temporary paths for other tools as needed. Do not use system-wide scratch directories or put scratch artifacts in the published site.

## Add or Edit a Page

Put pages directly in `content/`; nested directories are not discovered by the Makefile. For example, `content/example-page.md` renders to `docs/example-page/index.html`, available at `/example-page/`.

```markdown
---
title: Example page
---

# Example page

Page text with an [internal link](/instruments/).

![Description of the image](/assets/images/example.png)
```

Keep existing slugs such as `/joinus/` stable. The home page and error page are special: `content/index.md` renders to `docs/index.html`, and `content/404.md` renders to `docs/404.html`.

Add public navigation links in `theme/nav.html`. Shared markup belongs in `theme/`, presentation in `assets/style.css`, and scripts in `assets/js/`. Follow existing indentation and formatting; no formatter or linter is configured.

## Equations and Marginalia

The build enables Pandoc's dollar and single-backslash math delimiters and loads MathJax for pages containing equations. The versionless CDN URL deliberately follows upstream releases automatically, including major updates. Use `$S/N$` inline or a display block:

```markdown
\[
C = B \log_2\left(1+\frac{S}{N}\right)
\]
```

Keep display equations centered. A commentary block becomes a collapsible note:

```markdown
:::commentary
**A concise note title**

Supporting explanation belongs here.
:::
```

Place the block near the paragraph it explains. On desktop, the main body stays centered while notes sit to its right and may extend outside the viewport. At widths below 961px, notes appear in the normal flow. `filters/marginalia.lua` produces the markup; `assets/js/marginalia.js` handles positioning, collision avoidance, and the navigation toggle.

## Validate and Publish

Run `make check` for site changes. After removing or renaming a page, run `make rebuild` first: incremental builds do not remove old page directories. Review the diff for broken URLs, unexpected generated changes, and whitespace errors with `git diff --check`.

There is no unit, browser, or link-checking suite. Preview affected pages with `make serve`. For shared style or template changes, check the home page, People, and a page with marginalia on desktop and mobile. Verify compact header/footer spacing, image loading, centered equations, and individual and global note toggles when affected.

GitHub Pages publishes the committed `docs/` directory. Include regenerated output with site source changes. Edit the publication domain only in the root `CNAME` file; the build copies it into `docs/`. Keep contributor documentation and plans outside `docs/`.

## Commits and Pull Requests

Use short, capitalized, imperative commit subjects, for example `Update people page`. Keep each change focused and include its generated output. Pull requests should describe the change, affected pages, checks performed, and related issues or requests. Include screenshots for visual changes.
