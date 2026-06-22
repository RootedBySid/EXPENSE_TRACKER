
from pydantic import BaseModel,Field

class post(BaseModel):
    # id: int 
    expense: str
    Amount: int  = Field(ge=0)
    
class user_data(BaseModel):
    # id:int=Field(g=0)
    username:str =Field(min_length=1, max_length=75)
    password :str=Field(min_length=4)