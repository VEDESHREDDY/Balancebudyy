import os

class Config:
    SECRET_KEY = os.urandom(24)  # Secret key for sessions
    SQLALCHEMY_DATABASE_URI = 'sqlite:///fitfusion.db'  # Using SQLite for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False
