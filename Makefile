.PHONY: install dev build test clean format

install:
	npm install
	uv sync

dev:
	make start-backend &
	npm run dev

start-backend:
	./.venv/bin/uvicorn api.main:app --reload

build:
	npm run build

test:
	# Add Python tests here if any
	# uvx pytest
	# Add frontend tests here if any

clean:
	rm -rf dist .astro node_modules
	uv clean

format:
	# Add Python formatting here if needed
	# uvx ruff check . --fix
	# uvx ruff format .
	# Add frontend formatting here if needed
