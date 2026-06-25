from fastapi import APIRouter, Depends, HTTPException
from Models import post
from Utils.db_DI import get_db
from Schemas import expense_input
router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

@router.get("/")
def expenses(db=Depends(get_db)):
    return db.query(expense_input).all()

@router.get("/total")
def total(db=Depends(get_db)):
    total=0
    for exp in db.query(expense_input).all():
        total = total+exp.Amount
        
    return {"Total amount " : total}
    
    
@router.get("/search")
def search(q:str, db=Depends(get_db) ):
   
    exp=db.query(expense_input).filter(expense_input.expense==q).all()
    if exp:
        return exp
        
    raise HTTPException(status_code=404 ,detail="Expense not found")
    
@router.post("/")
def add_expense(data:post, db=Depends(get_db)):
        new_expense=expense_input(expense=data.expense , Amount=data.Amount)
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)
        return {"Added":new_expense}
@router.get("/{expense_id}")
def get_one_expense(expense_id:int, db=Depends(get_db)):
    single_exp=db.query(expense_input).filter(expense_input.id==expense_id).first()
    if single_exp:
        return single_exp
    raise HTTPException(status_code=404 ,detail="Expense not found")
    

@router.put("/{expense_id}")
def update_expense(expense_id:int ,data:post, db=Depends(get_db)):
    expenseUD=db.query(expense_input).filter(expense_input.id==expense_id).first()
    if expenseUD:
        expenseUD.expense=data.expense
        expenseUD.Amount=data.Amount
        db.commit()
        db.refresh(expenseUD)
        return {"Updated":expenseUD}
    raise HTTPException(status_code=404 ,detail="Expense not found")


@router.delete("/{expense_id}")
def delete_expense(expense_id:int, db=Depends(get_db)):
    expenseDL=db.query(expense_input).filter(expense_input.id==expense_id).first()
    if expenseDL:
        db.delete(expenseDL)
        db.commit()
        return {"status":"expense deleted"}
    raise HTTPException(status_code=404 ,detail="Expense not found")