from jose import jwt
from datetime import datetime, timedelta

# MUST match the SECRET_KEY and ALGORITHM in auth.py
SECRET_KEY = "forauthorisedpersononly"
ALGORITHM = "HS256"

def create_token():
    expire = datetime.utcnow() + timedelta(hours=1)
    payload = {
        "sub": "internal_user",
        "exp": expire
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

if __name__ == "__main__":
    print("Your JWT token:")
    print(create_token())
