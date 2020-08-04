from pydantic import BaseModel
from _datetime import date



class CustomerDetails(BaseModel):
    s_no:int
    rec_no:int
    address:str
    type_of_membership:str
    documents:bool
    user_agreement:bool
    account_no:int
    name_of_user:str
    phone_no:int
    dob:date
    email:str
    gender:str
    account_creation_date:date
    
    class Config:
        orm_mode = True


class CustomerCreate(CustomerDetails):
    pass

    class Config:
        orm_mode = True

