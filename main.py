from fastapi import FastAPI

from database import engine,base


from Routers import auth
from Routers import expenses


app=FastAPI()
base.metadata.create_all(bind=engine)







app.include_router(auth.router)
app.include_router(expenses.router)
    


