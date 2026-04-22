from sqlmodel import Field, SQLModel
from uuid import uuid4

class TransferJobItem(SQLModel, table=True):
    __tablename__ = "transfer_job_items"

    item_id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    job_id: str = Field(foreign_key="transfer_jobs.job_id")
    row_id: str