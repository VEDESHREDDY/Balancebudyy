from sqlalchemy import Column, Integer, String
from database import Base
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    # If you have a relationship with fitness plans, you can add it here
    fitness_plans = db.relationship('FitnessPlan', backref='user', lazy=True)

class FitnessPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan_name = db.Column(db.String(100), nullable=False)
    duration_weeks = db.Column(db.Integer, nullable=False)
    calories_target = db.Column(db.Float, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Define the User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))

# Define the Exercise model (optional, depending on your project)
class Exercise(Base):
    __tablename__ = 'exercises'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(255))
    duration = Column(Integer)  # Duration in minutes
