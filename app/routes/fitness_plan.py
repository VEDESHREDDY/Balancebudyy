from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/plans", tags=["Fitness Plans"])

@router.post("/", response_model=schemas.FitnessPlanResponse)
def create_plan(plan: schemas.FitnessPlanCreate, db: Session = Depends(database.get_db)):
    new_plan = models.FitnessPlan(**plan.dict())
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)
    return new_plan

@router.get("/", response_model=list[schemas.FitnessPlanResponse])
def get_plans(user_id: int, db: Session = Depends(database.get_db)):
    return db.query(models.FitnessPlan).filter(models.FitnessPlan.user_id == user_id).all()
