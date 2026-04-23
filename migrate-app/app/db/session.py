from app.db.metadata import pg_metadata
from app.config.settings import get_settings
from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine

settings = get_settings()

pg_engine = create_engine(url=settings.pg_url)

def create_pg():
    pg_metadata.create_all(pg_engine)

def get_pg_session():
    with Session(pg_engine) as session:
        yield session

RequiresPostgres = Annotated[Session, Depends(get_pg_session)]

rds_engine = create_engine(url=settings.rds_url)

def get_rds_session():
    with Session(rds_engine) as session:
        yield session

RequiresRDS = Annotated[Session, Depends(get_rds_session)]
