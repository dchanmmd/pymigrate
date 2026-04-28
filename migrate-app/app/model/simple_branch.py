from app.db.metadata import rds_metadata
from sqlmodel import SQLModel

class SimpleBranch(SQLModel):
    metadata = rds_metadata
    id: int
    name: str