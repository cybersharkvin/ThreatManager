.PHONY: test lint build

test:
./tests/go-test.sh
pytest tests

lint:
echo "TODO: run linters"

build:
docker build -t mcp-core ./core
