import bcrypt

from fastapi import FastAPI
from Models import User
from db_ops import insert_user

app = FastAPI()


@app.get("/login")
async def root(user: User):
    pass


@app.post("/signup")
async def create_user(user: User):
    username = user.username
    password = user.password
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    response = insert_user(username, hashed_password)
    return response
