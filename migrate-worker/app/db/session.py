from contextlib import contextmanager
from typing import Generator
from sqlalchemy import MetaData
from sqlalchemy.orm import Session
from app.config.app_environment import env
from sqlalchemy import create_engine

pg_engine = create_engine(env.pg_url)
my_engine = create_engine(env.rds_url)

pg_metadata = MetaData()
my_metadata = MetaData()

@contextmanager
def get_pg_session() -> Generator[Session]:
    session = Session(pg_engine)
    try:
        yield session
    finally:
        session.close()

@contextmanager
def get_my_session() -> Generator[Session]:
    session = Session(my_engine)
    try:
        yield session
    finally:
        session.close()