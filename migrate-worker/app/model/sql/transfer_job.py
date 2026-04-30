from datetime import datetime

from sqlmodel import Column, Enum, Field, SQLModel
from typing import Optional
from app.model.sql.job_result import JobResult
from app.model.sql.job_status import JobStatus

class TransferJob(SQLModel, table=True):
    __tablename__ = 'transfer_jobs'
    
    job_id: str = Field(primary_key=True)
    owner_id: str = Field()
    status: JobStatus = Field(sa_column=Column(Enum(JobStatus, name='job_status')))
    result: Optional[JobResult] = Field(sa_column=Column(Enum(JobResult, name='job_result')))
    pushed_at: datetime = Field()
    shifted_at: Optional[datetime] = Field()
    completed_at: Optional[datetime] = Field()
    retries: int = Field()
    error: Optional[str] = Field()