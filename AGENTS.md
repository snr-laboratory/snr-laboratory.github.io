# Repository Guidelines

## Scope and References

These instructions apply throughout the repository. Read [CONTRIBUTING.md](CONTRIBUTING.md) for authoring examples, commands, and review conventions. The [Makefile](Makefile) defines the build. Keep this file focused on durable rules; put task-specific plans in separate files when needed.

## Source of Truth

- `content/*.md`: Pandoc pages rendered to `docs/<slug>/index.html`. Exceptions: `index.md` becomes `docs/index.html`; `404.md` becomes `docs/404.html`.
- `theme/`: HTML template, navigation, and footer partials.
- `filters/marginalia.lua`: commentary markup conversion.
- `assets/`: shared CSS, JavaScript, and images; copied to `docs/assets/`.
- Root `CNAME`: publication domain; copied to `docs/CNAME`.
- `docs/`: committed GitHub Pages output. Generate it through Make; edit the source files.

## Change Rules

- Inspect `git status` before editing and preserve unrelated changes.
- Keep page files directly under `content/`; the build does not discover nested pages. Use lowercase, hyphenated names for new pages and preserve existing URL slugs unless a rename is requested.
- Use YAML `title` metadata and a matching top-level heading. Follow nearby formatting; keep shared presentation in `theme/` and `assets/`.
- Use root-relative internal URLs such as `/instruments/` and `/assets/images/example.png`. Update `theme/nav.html` when navigation changes.
- Preserve the established typography, palette, compact header/footer spacing, and centered display equations.
- Keep the main body centered independently of marginalia. Desktop notes sit beyond its right edge and may extend outside the viewport. Below 961px they return inline; keep CSS and JavaScript breakpoints synchronized.
- Write notes as `:::commentary` blocks with a bold title first. Layout and global toggle behavior live in `assets/js/marginalia.js`.

## Tools and Coding

- Write scripts and Make recipes for POSIX `sh`. Prefer standard utilities such as `sed`, `awk`, `grep`, and `find`; avoid Bash-only syntax and GNU-only flags in portable automation.
- Invoke Python explicitly as `$HOME/Applications/appvenv/bin/python`. `make serve` defaults to this interpreter; `PYTHON=/path/to/python` is an explicit override. Avoid Conda and silent changes to the shared environment.
- Keep scratch files, temporary builds, downloads, browser profiles, and screenshots in repository-local `build/`, `tmp/`, or `work/`. Never use system-wide scratch directories such as `/tmp`, `/private/tmp`, or `/var/tmp`. Set tool temporary-directory options and `TMPDIR` explicitly when needed; keep scratch out of published `assets/` and `docs/`.
- Prefer existing local tools under `$HOME/Applications/` and `/opt/OpenICEDA` before adding dependencies. See [the computing guide](content/computing.md) for installation and environment conventions.
- For new compiled helpers, strongly prefer C11 or later; avoid C++. Use STB-style implementation macros, explicit struct-based dynamic arrays, and arenas instead of scattered `malloc`/`free`. For MCU code, reserve bounded storage before acquisition and avoid heap allocation in interrupts or time-critical loops.
- Give agent tasks concrete goals and verification commands. Review generated code and dependencies; report actual check results and remaining uncertainties.

## Validation and Handoff

- Run `make check` after site changes. It builds and checks the home page, 404 page, and matching `CNAME`; it does not validate links or visual layout.
- After deleting or renaming pages, run `make rebuild` before `make check` to remove stale output.
- Preview visual changes with `make serve` on desktop and mobile; check math and marginalia when affected.
- Review `git diff --check` and the final diff. Include regenerated `docs/` changes with their source changes.
- Report what changed, which checks ran, and any validation gaps.
