# fastapi-htmx-tailwind

Experimenting rendering tabs using FastAPI and HTMX.

- [fastapi-htmx-tailwind](#fastapi-htmx-tailwind)
  - [Prerequisites](#prerequisites)
    - [1. Install runtimes](#1-install-runtimes)
    - [2. Install Python dependencies](#2-install-python-dependencies)
    - [3. Install Node dependencies](#3-install-node-dependencies)
  - [Run example](#run-example)
    - [Run the TailwindCSS watcher](#run-the-tailwindcss-watcher)
    - [Run backend server](#run-backend-server)

## Prerequisites

### 1. Install runtimes

**MacOS using brew**

```bash
brew install python@3.13 uv node@22
```

### 2. Install Python dependencies

```bash
uv sync
```

### 3. Install Node dependencies

```bash
cd ui/static
npm install
```

## Run example

### Run the TailwindCSS watcher

```bash
cd ui/static
npx tailwindcss -i ./css/input.css -o ./dist/output.css --watch
```

### Run backend server

```bash
source .venv/bin/activate
fastapi dev main.py
```

The example should run on http://127.0.0.1:8000
