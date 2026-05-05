from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

class Postgres(DeclarativeBase):
    metadata = MetaData()