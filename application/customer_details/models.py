
from sqlalchemy import Column, Integer, String, BigInteger, Boolean, Date

from application.customer_details.database import Base

class CustomerDetails(Base):
    __tablename__ = "customer_details"

    s_no=Column(Integer)
    rec_no=Column(Integer)
    address=Column(String(50))
    type_of_membership = Column(String(50))
    documents=Column(Boolean)
    user_agreement=Column(Boolean)
    account_no=Column(Integer, primary_key=True, index=True)
    name_of_user = Column(String(50))
    phone_no= Column(BigInteger)
    dob = Column(Date())
    email= Column(String(50))
    gender = Column(String(20))
    account_creation_date=Column(Date())

