from fastapi import FastAPI
import requests
from Data import Expenses,ID
from models import post
app=FastAPI()


@app.get("/expenses")
def expenses():
    return Expenses

@app.get("/expenses/total")
def total():
    total=0
    for expense in Expenses:
        total=total+expense.get("Amount")
    return {"Total amount ": total}
    
    
@app.get("/expenses/search")
def search(expense_query:str ):
    for expense in Expenses:
        if expense.get("expense") == expense_query.capitalize() or expense.get("expense")==expense_query.lower():
            return expense
    return "EXPENSE NOT FOUND"
    
@app.get("/expenses/{expense_id}")
def get_one_expense(expense_id:int):
    for expense in Expenses:
        if expense.get("id")==expense_id:
            return expense
    return "Expense not found"

@app.post("/add_expense")
def add_expense(data:post):
    for expense in Expenses:
        if data.model_dump().get("id") == expense.get("id") :
            return "Expense already exists"
    Expenses.append(data.model_dump())
    return {"added_expense":data.model_dump()}


@app.put("/update_expense/{expense_id}")
def update_expense(expense_id:int ,data:post):
    for index,expense in enumerate(Expenses):
        if expense.get("id") == expense_id:
            expense[index]=data.model_dump()
            return {"status":"Expense Updated"}
    return "Not found expense to be updated"


@app.delete("/delete_expense/{expense_id}")
def delete_expense(expense_id:int):
    for index,expense in enumerate(Expenses):
        if expense.get("id") == expense_id:
            Expenses.pop(index)
            return {"status":"Expense Deleted"}
    return "Expense ID not found to delete"
    
    
