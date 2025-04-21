# Makefile for the Email_Crafter project

# Variables
PROJECT_NAME = emailcrafter
PYTHON = python3
PIP = pip
POETRY = poetry

# Targets
.PHONY: all setup install run clean test

all: setup install test

setup:
	@echo "Setting up virtual environment..."
	$(POETRY) env use $(PYTHON)

install:
	@echo "Installing dependencies..."
	$(POETRY) install

run-app:
	@echo "Running the application..."
	$(POETRY) run streamlit run src/app.py --server.port 8080

run-api:
	@echo "Running the API..."
	$(POETRY) run $(PYTHON) api/api.py

test:
	@echo "Running tests..."
	$(POETRY) run pytest -v tests/test.py

docker-build:
	@echo "Building Docker image..."
	docker-compose build

docker-run-app:
	@echo "Running application in Docker..."
	docker-compose up app

docker-run-api:
	@echo "Running application in Docker..."
	docker-compose up api

docker-test:
	@echo "Running tests in Docker..."
	docker-compose run test

docker-down:
	@echo "Running application in Docker..."
	docker-compose down

clean:
	@echo "Cleaning up..."
	$(POETRY) env remove $(PYTHON)

clear-cache:
	@echo "Cleaning up..."
	$(POETRY) cache clear --all .

