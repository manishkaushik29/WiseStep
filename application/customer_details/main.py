import uvicorn
from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from fastapi.encoders import jsonable_encoder

from application.customer_details import models, schemas
from application.customer_details.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def create_customer_item(db: Session, item: schemas.CustomerCreate):
    try:
        db_item = models.CustomerDetails(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        print("exception is :", e)


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")




@app.get("/details/")
def read_items(acc:int,db: Session = Depends(get_db)):
    records=db.query(models.CustomerDetails).filter(models.CustomerDetails.account_no == acc).first()
    return records




@app.post("/customer/")
def create_item_for_user(
    item: schemas.CustomerCreate, db: Session = Depends(get_db)
):
    return create_customer_item(db=db, item=item)





if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=8001, debug=True)



