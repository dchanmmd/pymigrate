from datetime import datetime, timezone
from typing import Optional
import uuid

from sqlalchemy import UUID, DateTime, Enum, Index, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.postgres import Postgres
from app.model.job_result import JobResult
from app.model.job_status import JobStatus

class TransferJob(Postgres):
    __tablename__ = 'transfer_jobs'
    __table_args__ = (Index('idx_jobs_status_pushed_at', 'status', 'pushed_at'),)

    job_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    owner_id: Mapped[str] = mapped_column(String, default='', nullable=False)
    status: Mapped[JobStatus] = mapped_column(Enum(JobStatus, name='job_status'), default=JobStatus.Pending, nullable=False)
    result: Mapped[Optional[JobResult]] = mapped_column(Enum(JobResult, name='job_result'), nullable=True)
    pushed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    shifted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    tries: Mapped[int] = mapped_column(Integer, default=0)
    error: Mapped[Optional[str]] = mapped_column(String, nullable=True)
