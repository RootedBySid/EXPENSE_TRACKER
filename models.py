from pydantic import BaseModel,Field
from Data import ID
class post(BaseModel):
    id: int 
    expense: str
    Amount: int  = Field(ge=0)