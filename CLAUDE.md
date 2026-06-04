# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

All tasks run via `mise run <task>`. The toolchain (Python 3.14, uv, bun) is pinned in `mise.toml`.

| Task | Command |
|---|---|
| Install Python deps | `mise run install` |
| Install JS deps | `mise run install:js` |
| Dev server | `mise run dev` |
| Production server | `mise run serve` |
| Build CSS | `mise run build:css` |
| Format | `mise run fmt` |
| Lint | `mise run lint` |
| Type check | `mise run typecheck` |
| Vulnerability audit | `mise run vuln` |
| Upgrade Python deps | `mise run deps` |

## Architecture

`main.py` owns the FastAPI application at the repo root. It serves three tabs via HTMX:

- `/` — main index page
- `/tab1` — static HTML tab
- `/tab2` — generates a fake data table with Polars and Faker, rendered server-side
- `/tab3` — static HTML tab

Templates live in `ui/templates/`. Static assets (JS, CSS) live in `ui/static/`.

`ui/static/src/input.css` is the Tailwind CSS entry point; the compiled output goes to `ui/static/src/output.css` (gitignored). Run `mise run build:css` before starting the server. HTMX and DaisyUI are installed as local JS dependencies via bun.
