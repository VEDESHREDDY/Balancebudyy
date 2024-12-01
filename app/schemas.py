from pydantic import BaseModel, EmailStr
from typing import List

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class FitnessPlanBase(BaseModel):
    plan_name: str
    duration_weeks: int
    calories_target: float

class FitnessPlanCreate(FitnessPlanBase):
    user_id: int

class FitnessPlanResponse(FitnessPlanBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
