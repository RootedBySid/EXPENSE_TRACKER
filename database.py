from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="postgresql://postgres:comegetme@localhost:5432/SiddhantYadav"

engine=create_engine(DATABASE_URL)
SessionLocal= sessionmaker(autoflush=False , autocommit=False,bind=engine)
base=declarative_base()