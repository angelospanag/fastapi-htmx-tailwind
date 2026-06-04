# fastapi-htmx-tailwind

Experimenting with rendering tabs using FastAPI and HTMX.

<!-- TOC -->
* [fastapi-htmx-tailwind](#fastapi-htmx-tailwind)
  * [Getting Started](#getting-started)
  * [Development](#development)
<!-- TOC -->

## Getting Started

[`mise`](https://mise.jdx.dev/) manages the pinned toolchain (Python 3.14, uv, bun).

**macOS / Linux**

```bash
curl https://mise.run | sh
```

**Windows**

```bash
winget install jdx.mise
```

Activate mise in your shell so the pinned versions take precedence over any system installs (Homebrew, etc.). In `~/.zshrc`:

```bash
eval "$(mise activate zsh)"
```

Then, in the repo:

```bash
mise trust           # one-time, confirms you trust this repo's mise.toml
mise install         # downloads and pins Python, uv, and bun
mise run install     # installs Python dependencies into .venv
mise run install:js  # installs JS dependencies
mise run build:css   # compiles Tailwind CSS
mise run dev         # starts the dev server on http://127.0.0.1:8000
```

## Development

| Command                | Description                              |
|------------------------|------------------------------------------|
| `mise run install`     | Install Python dependencies into `.venv` |
| `mise run install:js`  | Install JS dependencies                  |
| `mise run dev`         | FastAPI dev server on 127.0.0.1:8000     |
| `mise run serve`       | Production server on 0.0.0.0:8000        |
| `mise run build:css`   | Compile Tailwind CSS                     |
| `mise run fmt`         | Format code via `ruff format`            |
| `mise run lint`        | Lint code via `ruff check`               |
| `mise run typecheck`   | Type check via `ty check`                |
| `mise run test`        | Run tests                                |
| `mise run vuln`        | Audit deps for known vulnerabilities     |
| `mise run deps`        | Update and sync Python dependencies      |
