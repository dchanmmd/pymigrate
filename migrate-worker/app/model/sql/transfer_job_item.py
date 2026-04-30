from app.model.sql.item_result import ItemResult
from sqlmodel import Column, Enum, Field, SQLModel

class TransferJobItem(SQLModel, table=True):
    __tablename__ = 'transfer_job_items'

    item_id: str = Field(primary_key=True)
    job_id: str = Field(foreign_key='transfer_jobs.job_id')
    row_id: str = Field()
    result: ItemResult = Field(sa_column=Column(Enum(ItemResult, name='item_result')))