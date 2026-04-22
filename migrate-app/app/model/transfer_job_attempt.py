from app.model.job_status import JobStatus
from datetime import datetime, timezone
from sqlmodel import Column, Enum, Field, SQLModel
from uuid import uuid4

class TransferJobAttempt(SQLModel, table=True):
    __tablename__ = "transfer_job_tries"

    attempt_id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    job_id: str = Field(foreign_key="transfer_jobs.job_id")
    started_at: datetime = Field(default=datetime.now(timezone.utc))
    completed_at: datetime | None = None
    status: JobStatus = Field(sa_column=Column(Enum(JobStatus, name="job_status"), nullable=False))
    error: str | None = None