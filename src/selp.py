from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: int
    qnt: int


products: List[Product] = []

api = FastAPI()


@api.get("/")
def home():
    return {"message": "Inventory Management System"}


@api.get("/products")
def get_products():
    return products

@api.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"message": "Error: Product not found"}


@api.post("/products")
def add_product(product: Product):
    products.append(product)
    return {"message": "Added successfully", "product": product}


@api.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for index, existing_product in enumerate(products):
        if existing_product.id == product_id:
            products[index] = updated_product
            return {"message": "Updated successfully", "product": updated_product}
    return {"message": "Error: Product not found"}


@api.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, existing_product in enumerate(products):
        if existing_product.id == product_id:
            products.pop(index)
            return {"message": "Deleted successfully"}
    return {"message": "Error: Product not found"}

