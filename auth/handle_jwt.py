import time
import os
import jwt
from dotenv import load_dotenv

load_dotenv()
SECRET = os.getenv("SECRET")
ALGORITHM = os.getenv("ALGORITHM")


def get_token(token: str):
    return {
        "token": token
    }


def get_jwt(username: str):
    payload = {
        "username": username,
        "expiry": time.time() + 3600
    }
    token = jwt.encode(payload, SECRET, ALGORITHM)
    return get_token(token)


def decode_jwt(token: str):
    try:
        decode_token = jwt.decode(token, SECRET, ALGORITHM)
        if decode_token.get["expires"] >= time.time():
            return decode_token
    except Exception:
        return {}
