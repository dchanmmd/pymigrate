import uuid
from sqlalchemy import UUID, Index, String, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.db.postgres import Postgres
from app.model.item_result import ItemResult

class TransferJobItem(Postgres):
    __tablename__ = 'transfer_job_items'
    __table_args__ = (Index('idx_items_job_id_result', 'job_id', 'result'),)

    item_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    job_id: Mapped[str] = mapped_column(String, ForeignKey('transfer_jobs.job_id'), nullable=False)
    row_id: Mapped[str] = mapped_column(String, nullable=False)
    result: Mapped[ItemResult] = mapped_column(Enum(ItemResult, name='item_result'), default=ItemResult.Pending, nullable=False)