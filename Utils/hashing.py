from passlib.context import  CryptContext



pwd_context=CryptContext(schemes=["bcrypt"] , deprecated="auto")

def verify_user(pass_entered,pass_stored):
    return pwd_context.verify(pass_entered,pass_stored)