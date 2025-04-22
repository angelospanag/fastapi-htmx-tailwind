# fastapi-htmx-tailwind

Experimenting rendering tabs using FastAPI and HTMX.

<!-- TOC -->
* [fastapi-htmx-tailwind](#fastapi-htmx-tailwind)
  * [Prerequisites](#prerequisites)
    * [1. Install runtimes](#1-install-runtimes)
    * [2. Install Python dependencies](#2-install-python-dependencies)
    * [3. Install Node dependencies](#3-install-node-dependencies)
  * [Run example](#run-example)
    * [Build CSS](#build-css)
    * [Run development server](#run-development-server)
    * [Run production server](#run-production-server)
<!-- TOC -->

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

### Build CSS

```bash
cd ui/static
npm run build:css
```

### Run development server

```bash
uv run fastapi dev main.py
```

### Run production server

```bash
uv run fastapi run main.py
```

The example should run on http://127.0.0.1:8000
