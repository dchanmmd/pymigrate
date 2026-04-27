from app.db.metadata import pg_metadata
from app.model.job_result import JobResult
from app.model.job_status import JobStatus
from datetime import datetime, timezone
from sqlmodel import Enum
from uuid import uuid4

from sqlmodel import Field, SQLModel

class TransferJob(SQLModel, table=True):
    metadata = pg_metadata
    __tablename__ = 'transfer_jobs'
    job_id: str = Field(default_factory= lambda: str(uuid4()), primary_key=True)
    status: JobStatus = Field(default=JobStatus.Pending, sa_column=Enum(JobStatus, name='job_status'))
    result: JobResult | None = Field(default=None, sa_column=Enum(JobResult, name='job_result'))
    pushed_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    shifted_at: datetime | None = None
    completed_at: datetime | None = None
    retries: int = Field(default=0)
    error: str | None = None