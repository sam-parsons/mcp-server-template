.PHONY: test build clean docker-build docker-run

# Run tests
test:
	pytest

# Build the Python package
build:
	uv build

# Clean up build artifacts and cache files
clean:
	rm -rf dist/ build/ *.egg-info/ htmlcov/ .coverage .pytest_cache/ __pycache__/ .ruff_cache/

# Build Docker image locally
docker-build:
	docker build -t nhl-api-mcp .

# Run Docker container on port 8000
docker-run:
	docker run -d -p 8000:8000 --name nhl-api-mcp nhl-api-mcp
