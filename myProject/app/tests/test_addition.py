from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime

client = TestClient(app)

def test_add_numbers_success():
    response = client.post("/add", json={"batchid": "id0101", "payload": [[1, 2], [3, 4]]})
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["response"] == [3, 7]
    assert data["status"] == "complete"
    assert "started_at" in data
    assert "completed_at" in data

def test_add_numbers_empty_payload():
    response = client.post("/add", json={"batchid": "id0102", "payload": []})
    assert response.status_code == 422  # Validation error due to empty payload

def test_add_numbers_invalid_type():
    response = client.post("/add", json={"batchid": "id0103", "payload": [[1, "a"], [3, 4]]})
    assert response.status_code == 422  # Validation error due to wrong type
