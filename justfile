set shell := ["zsh", "-cu"]
export UV_CACHE_DIR := ".uv-cache"

default:
  @just --list

sync:
  uv sync

build:
  uv run python build.py

clean:
  rm -f index.html hello-world.html

serve:
  python3 -m http.server 8000

rebuild: sync build
