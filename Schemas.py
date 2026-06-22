from database import base
from sqlalchemy import Column, Integer, String, func

class expense_input(base):
    
    __tablename__ ="expenses"
    
    id= Column(Integer, primary_key=True )
    expense=Column(String)
    Amount=Column(Integer)
    
    
class User(base):
    __tablename__ ="users"
    
    id=Column(Integer,primary_key=True )
    username=Column(String,unique=True, nullable=False)
    password=Column(String, nullable=False)
    