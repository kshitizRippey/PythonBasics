from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class CreateOrder(BaseModel):
    token: str
    quantity: int
    product_id: int


class UpdateOrder(BaseModel):
    token: str
    order_id: int
    quantity: int


class Order(BaseModel):
    token: str
    order_id: int
