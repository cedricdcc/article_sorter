# Makefile for testing the Docker stack

DATA_VOLUME ?= ./data

build:
	docker-compose build

run:
	docker-compose up

setup-ollama:
bash setup_ollama.sh

test:
@echo "Testing the Docker stack..."
@$(MAKE) setup-ollama
@$(MAKE) build
@$(MAKE) run

clean:
	docker-compose down
	docker-compose rm -f
	docker system prune -f
