import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_CONN = "postgresql://postgres:123456@127.0.0.1:5432/wisestep"

#SQLALCHEMY_DATABASE_URL = os.getenv(DB_CONN)

try:
    engine = create_engine(DB_CONN, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    print("connection successful")



except Exception as err:
    #print(e.with_traceback())
    err_type, err_obj, traceback = sys.exc_info()
    print(traceback.tb_lineno)
    print(err)



Base = declarative_base()