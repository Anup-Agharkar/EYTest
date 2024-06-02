# FastAPI Addition Service

This is a FastAPI-based service that provides an endpoint for adding lists of integers using multiprocessing. The project is structured using the MVC (Model-View-Controller) pattern.

## Features

- FastAPI framework for quick and efficient API development.
- Pydantic models for request and response validation.
- Multiprocessing for efficient computation.
- Comprehensive error handling and logging.
- Unit tests for all edge cases and scenarios.

## Project Structure
myProject/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── controllers/
│ │ ├── init.py
│ │ ├── addition_controller.py
│ ├── models/
│ │ ├── init.py
│ │ ├── request_model.py
│ │ ├── response_model.py
│ ├── services/
│ │ ├── init.py
│ │ ├── addition_service.py
│ ├── tests/
│ ├── init.py
│ ├── test_addition.py
└── requirements.txt


## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic
- Pytest
- Requests

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/fastapi-addition-service.git
    cd fastapi-addition-service
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the FastAPI server, run:

```bash
uvicorn app.main:app --reload


Example Request
Using requests library in Python:

import requests

url = "http://127.0.0.1:8000/add"
headers = {
    "x-client-id": "my-client-id"
}
data = {
    "batchid": "id0101",
    "payload": [[1, 2], [3, 4]]
}

response = requests.post(url, json=data, headers=headers)
print(response.json())

Running Tests
To run the tests, use:
pytest app/tests/test_addition.py

