from app.db.metadata import pg_metadata
from app.model.item_result import ItemResult
from sqlmodel import Enum, Field, SQLModel
from uuid import uuid4

class TransferJobItem(SQLModel, table=True):
    metadata = pg_metadata
    __tablename__ = 'transfer_job_items'
    item_id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    job_id: str = Field(foreign_key='transfer_jobs.job_id')
    row_id: str = Field()
    result: ItemResult = Field(default=ItemResult.Pending, sa_column=Enum(ItemResult, name='item_result'))