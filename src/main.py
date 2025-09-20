from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    title: str
    description: str

todos: List[Todo] = []

api= FastAPI()

@api.get("/")
def home():
    return {"message": "Hello, World!"}

@api.get("/todo")
def get_todo():
    return todos

@api.post("/todo")
def post_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo added successfully", "todo": todo}

@api.put("/todo/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, existing_todo in enumerate(todos):
        if existing_todo.id == todo_id:
            todos[index] = updated_todo
            return {"message": "Todo updated successfully", "todo": updated_todo}
    return {"message": "Error in Updation"}

@api.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    for index, existing_todo in enumerate(todos):
        if existing_todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted successfully"}
    return {"message": "Error in deletion"}