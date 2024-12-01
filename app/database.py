from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace these with your MySQL credentials
DATABASE_URL = "mysql+mysqlconnector://root:vedesh@123@localhost:3306/fitfusion_db"


# Create the SQLAlchemy engine to interact with the database
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)

# Create the session maker to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for models to inherit from
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
