import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from src.main import api

client = TestClient(api)

#test for home endpoint
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

#test post
def test_post_todo():
    response = client.post("/todo", json={"id": 1, "title": "Test Todo", "description": "This is a test todo"})
    assert response.status_code == 200
    assert response.json() == {"message": "Todo added successfully", "todo": {"id": 1, "title": "Test Todo", "description": "This is a test todo"}}
#tsest get
def test_get_todo():
    response = client.get("/todo")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "title": "Test Todo", "description": "This is a test todo"}]
#test put
def test_update_todo():
    client.post("/todo", json={"id": 2, "title": "Another Todo", "description": "This is another test todo"})
    response = client.put("/todo/2", json={"id": 2, "title": "Updated Todo", "description": "This todo has been updated"})
    assert response.status_code == 200
    assert response.json() == {"message": "Todo updated successfully", "todo": {"id": 2, "title": "Updated Todo", "description": "This todo has been updated"}}

#test delete
def test_delete_todo(): 
    response = client.delete("/todo/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted successfully"}