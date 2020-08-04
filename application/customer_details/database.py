import os
import sys

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_CONN = "postgresql://postgres:0510@127.0.0.1:5433/wisestep"

#SQLALCHEMY_DATABASE_URL = os.getenv(DB_CONN)

try:

    engine = create_engine(DB_CONN)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    print("connection successful")
    print(engine.table_names())
    m=MetaData()
    t=Table("customer_details",m,autoload=True, autoload_with=engine)
    print(repr(t))



except Exception as err:
    #print(e.with_traceback())
    err_type, err_obj, traceback = sys.exc_info()
    print(sys.exc_info())
    print(traceback.tb_lineno)



Base = declarative_base()