import os
import time
import jwt
from dotenv import load_dotenv

load_dotenv()
SECRET = os.getenv("SECRET")
ALGORITHM = os.getenv("ALGORITHM")


def sign_jwt(username: str):
    payload = {
        "username": username,
        "expiry": time.time() + 3600
    }
    token = jwt.encode(payload, SECRET, ALGORITHM)
    return token


def decode_jwt(token: str):
    try:
        decode_token = jwt.decode(token, SECRET, ALGORITHM)
        if decode_token.get["expires"] >= time.time():
            return decode_token
    except:
        return {}
