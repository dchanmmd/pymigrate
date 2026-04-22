from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine
import os

db_driver = os.getenv('DB_DRIVER')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

url = f"{db_driver}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(url=url)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

RequiresSession = Annotated[Session, Depends(get_session)]