from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setup the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:yourpassword@localhost/your_database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a User model (table)
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"

# Create the tables in the database
with app.app_context():
    db.create_all()  # Create all tables defined by models (in this case, 'users')

# API Route to Create a User
@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        # Get data from the request
        data = request.get_json()
        name = data.get('name')

        if not name:
            return jsonify({"error": "Name is required"}), 400
        
        # Create a new User instance
        new_user = User(name=name)

        # Add to the session and commit the transaction to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": f"User {name} created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Route to Get all Users
@app.route('/get_users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        users_list = [{"id": user.id, "name": user.name} for user in users]
        return jsonify({"users": users_list}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)

# Create tables in the database if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/create-user/")
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    db_user = models.User(username=username, email=email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/get-users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.get("/get-user/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/create-exercise/")
def create_exercise(name: str, description: str, duration: int, db: Session = Depends(get_db)):
    db_exercise = models.Exercise(name=name, description=description, duration=duration)
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

@app.get("/get-exercises/")
def get_exercises(db: Session = Depends(get_db)):
    exercises = db.query(models.Exercise).all()
    return exercises

@app.get("/get-exercise/{exercise_id}")
def get_exercise(exercise_id: int, db: Session = Depends(get_db)):
    exercise = db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise

from fastapi import FastAPI
from database import engine, Base
import models

# Create tables in the database (if they don't already exist)
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Balance Buddy !"}

