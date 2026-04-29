from app.db.metadata import pg_metadata
from app.model.job_result import JobResult
from app.model.job_status import JobStatus
from datetime import datetime, timezone
from sqlmodel import Column, Enum
from uuid import uuid4

from sqlmodel import Field, SQLModel

class TransferJob(SQLModel, table=True):
    metadata = pg_metadata
    __tablename__ = 'transfer_jobs'
    job_id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    owner_id: str = Field(default='')
    status: JobStatus = Field(sa_column=Column(Enum(JobStatus, name='job_status'), default=JobStatus.Pending, nullable=False))
    result: JobResult | None = Field(sa_column=Column(Enum(JobResult, name='job_result'), nullable=True))
    pushed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    shifted_at: datetime | None = None
    completed_at: datetime | None = None
    retries: int = Field(default=0)
    error: str | None = None