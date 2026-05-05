from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from sqlalchemy import DateTime, Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.postgres import Postgres
from app.model.job_result import JobResult
from app.model.job_status import JobStatus

class TransferJob(Postgres):
    __tablename__ = 'transfer_jobs'

    job_id: Mapped[str] = mapped_column(String, primary_key=True)
    owner_id: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[JobStatus] = mapped_column(Enum(JobStatus, name='job_status'))
    result: Mapped[Optional[JobResult]] = mapped_column(Enum(JobResult, name='job_result'))
    pushed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    shifted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    tries: Mapped[int] = mapped_column(Integer)
    error: Mapped[Optional[str]] = mapped_column(String)
