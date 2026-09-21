
run:
	uv run python -m src

debug:
	uv run python -m pdb src

install:
	uv sync

clean:
	rm -rf .mypy_cache
	rm -rf llm_sdk/__pycache__
	rm -rf src/__pycache__
	rm -rf src/.mypy_cache

lint:
	flake8 src
	mypy src --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs