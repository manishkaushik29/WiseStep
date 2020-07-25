
from sqlalchemy import Column, Integer, String, BigInteger,Boolean,Date
from application.fetch_data_based_on_acc_no.database import Base

class CustomerDetails(Base):
    __tablename__ = "customer_details"

    account_no= Column(Integer, primary_key=True, index=True)
    s_no =Column(Integer)
    rec_no =Column(Integer)
    address=Column(String(50))
    type_of_membership= Column(String(50))
    documents=Column(Boolean)
    user_agreement=Column(Boolean)
    email=Column(String(50))
    name_of_user=Column(String(50))
    phone_no=Column(BigInteger)
    dob=Column(Date())
    gender=Column(String(20))
    account_creation_date=Column(Date())