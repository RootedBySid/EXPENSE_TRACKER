from jose import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

SECRET_KEY="comegetme"
ALGORITHM="HS256"

def generate_token(data:dict):
    token= jwt.encode(  data, SECRET_KEY, algorithm=ALGORITHM)
    return token

def get_current_user(token:str = Depends(oauth2_scheme)):
    payload=jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get("sub")