from fastapi.testclient import TestClient
from src.main1 import api

client = TestClient(api)

# Test for home endpoint
def test_home():    
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Book Management System"}

# Test post
def test_post_book():
    response = client.post("/book", json={"id": 1, "name": "Test Book", "description": "This is a test book", "isAvailable": True})
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Test Book", "description": "This is a test book", "isAvailable": True}]

# Test get
def test_get_book():
    response = client.get("/book")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Test Book", "description": "This is a test book", "isAvailable": True}]

# Test put
def test_update_book(): 
    client.post("/book", json={"id": 2, "name": "Another Book", "description": "This is another test book", "isAvailable": False})
    response = client.put("/book/2", json={"id": 2, "name": "Updated Book", "description": "This book has been updated", "isAvailable": True})
    assert response.status_code == 200
    assert response.json() == {"id": 2, "name": "Updated Book", "description": "This book has been updated", "isAvailable": True}

# Test delete
def test_delete_book(): 
    response = client.delete("/book/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test Book", "description": "This is a test book", "isAvailable": True}