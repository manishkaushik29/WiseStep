from sqlalchemy import DateTime, BigInteger, Boolean, Date

from pydantic import BaseModel, ValidationError
from _datetime import date

class CustomerDetails(BaseModel):
    s_no: int
    rec_no: int
    address: str
    type_of_membership: str
    documents: bool
    user_agreement: bool
    account_no: int
    name_of_user: str
    phone_no: int
    dob: date
    email: str
    gender: str
    account_creation_date: date

    class Config:
        orm_mode = True


class CustomerCreate(CustomerDetails):
    pass

    class Config:
        orm_mode = True



'''
data = dict(
    s_no=1,
    rec_no=1234,
    address='a-1,institutional area',
    type_of_membership = 'cust',
    documents='True',
    user_agreement='True',
    account_no=21,
    name_of_user = 'ram',
    phone_no= '9823456178',
    dob ='2000-07-03',
    email = 'ram123@gmail.com',
    gender = 'Male',
    account_creation_date='2020-07-03'
)

try:
    CustomerDetails(**data)
    print('success')
except ValidationError as e:
    print(e)
'''