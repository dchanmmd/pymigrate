from sqlalchemy import Enum, ForeignKey, String
from app.db.postgres import Postgres
from app.model.item_result import ItemResult
from sqlalchemy.orm import Mapped, mapped_column

class TransferJobItem(Postgres):
    __tablename__ = 'transfer_job_items'
    item_id: Mapped[str] = mapped_column(String, primary_key=True)
    job_id: Mapped[str] = mapped_column(String, ForeignKey("transfer_jobs.job_id"))
    row_id: Mapped[str] = mapped_column(String)
    result: Mapped[ItemResult] = mapped_column(Enum(ItemResult, name='item_result', create_type=False))