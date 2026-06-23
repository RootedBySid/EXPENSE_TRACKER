
from fastapi import APIRouter, Depends, HTTPException

from Utils.db_DI import get_db
from Models import post,user_data
from Schemas import User

from Utils.hashing import  verify_user,pwd_context


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)




@router.post("/login")
def login(data:user_data, db=Depends(get_db)):
    user=db.query(User).filter(User.username==data.username).first()
    if user:
        if verify_user(data.password, user.password ):
            return{"Status":"Logged in"}
        raise HTTPException(status_code=401,detail="Incorrect password entered")
    raise HTTPException(status_code=404,detail="User does not exists")


@router.post("/register")
def register(data:user_data, db = Depends(get_db)):
    new_user=User(username=data.username, password =pwd_context.hash(data.password))
    existing_user=db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        return {"error":"User already exists"}
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"Status":f"Added user: {new_user.username}"}

#need to be fixedd