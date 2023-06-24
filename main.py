import bcrypt

from fastapi import FastAPI
from models import User
from db_ops import insert_user, get_stored_password
from auth.handle_jwt import sign_jwt

app = FastAPI()


@app.post("/signup")
async def create_user(user: User):
    username = user.username
    password = user.password
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    message = insert_user(username, hashed_password)
    return {"message": message}


@app.post("/login")
async def login(user: User):
    response = {"message": "User does not exist!", "access_token": ""}
    password = user.password
    password = password.encode('utf-8')
    hashed_password = get_stored_password(user.username)
    if hashed_password is not None:
        if bcrypt.checkpw(password, hashed_password):
            response["message"] = "Logged in successfully!"
            response["access_token"] = f"{sign_jwt(user.username)}"
        else:
            response["message"] = "Could not log in. Wrong Password!"
        return response
    return response


@app.post("/create")
async def create_order():
    pass


@app.get("/read")
async def read_order():
    pass


@app.patch("/update")
async def update_order():
    pass


@app.delete("/delete")
async def delete_order():
    pass
