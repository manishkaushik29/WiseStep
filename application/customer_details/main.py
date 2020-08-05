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

@app.put("/customer/{rec_no}", response_model=schemas.CustomerDetails)
def update_item(rec_no: int, item: schemas.CustomerDetails, db: Session = Depends(get_db)):
    update_item_encoded = jsonable_encoder(item)
    db.query(models.customerdetails).filter(models.customerdetails.rec_no==rec_no).update(dict(update_item_encoded))
    db.commit()
    return update_item_encoded

if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=8001, debug=True)



