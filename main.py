import bcrypt

from fastapi import FastAPI
from Models import User
from db_ops import insert_user, get_stored_password

app = FastAPI()


@app.post("/signup")
async def create_user(user: User):
    username = user.username
    password = user.password
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    response = insert_user(username, hashed_password)
    return response


@app.post("/login")
async def root(user: User):
    response = {"error": True, "message": "User does not exist!"}
    password = user.password.encode('utf-8')
    hashed_password = get_stored_password(user.username)
    if hashed_password is not None:
        if bcrypt.checkpw(password, hashed_password):
            response["error"] = False
            response["message"] = "Logged in successfully!"
        else:
            response["error"] = True
            response["message"] = "Could not log in. Wrong Password!"
        return response
    return response
