IMAGE_NAME=health-calculator-service
PORT=5000
.PHONY: init run test build clean
init:
@echo "Installing dependencies..."
pip install -r requirements.txt
run:
@echo "Running the Flask app..."
python app.py
test:
@echo "Running tests..."
python -m unittest discover
build:
@echo "Building the Docker image..."
docker build -t $(IMAGE_NAME) .