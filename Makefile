IMAGE_NAME=health-calculator-service
PORT=5000

.PHONY: init run test build clean

init:
	@echo "Installing dependencies..."
	python -m venv venv
	. venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt

run:
	@echo "Running the Flask app..."
	python app.py

test:
	@echo "Running tests..."
	. venv/bin/activate; \
	python -m pytest tests/ -v

build:
	@echo "Building the Docker image..."
	docker build -t $(IMAGE_NAME) .
