# main.py

import os
from datetime import time

from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlmodel import Field, Session, SQLModel, create_engine

import fhir.resources.fhirtypes
from fhir.resources.patient import Patient as PyPatient

class Patient(SQLModel, table=True):
    id: int = Field(primary_key=True)

#
# DATABASE: str = os.getenv("DATABASE", "db")
# DB_USER: str = os.getenv("DB_USER", "user")
# DB_PASSWORD: str = os.getenv("DB_PASSWORD", "password")
# DB_HOST: str = os.getenv("DB_HOST", "localhost")
# DB_PORT: str = os.getenv("DB_PORT", "5432")
#
# SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}"
SQLALCHEMY_DATABASE_URL = f"sqlite:///fhir.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Dependency
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


demo_router = SQLAlchemyCRUDRouter(
    schema=Patient,
    create_schema=PyPatient,
    db_model=Patient,
    db=get_db
)

app = FastAPI()
app.include_router(demo_router)


@app.on_event("startup")
async def startup_event():
    SQLModel.metadata.create_all(engine)

