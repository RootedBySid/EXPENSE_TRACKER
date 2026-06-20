from fastapi import FastAPI, HTTPException
import requests
from Data import Expenses,ID
from Pydantic_models import post
from DB_MODELS import expense_input,func
from database import base, engine, SessionLocal

app=FastAPI()
db=SessionLocal()
base.metadata.create_all(bind=engine)

@app.get("/expenses")
def expenses():
    return db.query(expense_input).all()

@app.get("/expenses/total")
def total():
    total=0
    for exp in db.query(expense_input).all():
        total = total+exp.Amount
        
    return {"Total amount " : total}
    
    
@app.get("/expenses/search")
def search(q:str ):
   
    exp=db.query(expense_input).filter(expense_input.expense==q).all()
    if exp:
        return exp
        
    return {"error":"expense not found"}
    
@app.post("/add_expense")
def add_expense(data:post):
    new_expense=expense_input(expense=data.expense , Amount=data.Amount)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return {"Added":new_expense}

@app.get("/expenses/{expense_id}")
def get_one_expense(expense_id:int):
    single_exp=db.query(expense_input).filter(expense_input.id==expense_id).first()
    if single_exp:
        return single_exp
    return {"error":"Expense not found"}
   
    
    
    

@app.put("/update_expense/{expense_id}")
def update_expense(expense_id:int ,data:post):
    expenseUD=db.query(expense_input).filter(expense_input.id==expense_id).first()
    if expenseUD:
        expenseUD.expense=data.expense
        expenseUD.Amount=data.Amount
        db.commit()
        db.refresh(expenseUD)
        return {"Updated":expenseUD}
        


@app.delete("/delete_expense/{expense_id}")
def delete_expense(expense_id:int):
    expenseDL=db.query(expense_input).filter(expense_input.id==expense_id).first()
    if expenseDL:
        db.delete(expenseDL)
        db.commit()
        return {"status":"expense deleted"}
    return {"error":"EXpense not found "}
