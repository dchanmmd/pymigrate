from dataclasses import dataclass
from app.schema.job_item import JobItem
from app.model.sql.job_result import JobResult
from app.model.sql.job_status import JobStatus
from datetime import datetime
from typing import Optional

@dataclass
class ItemizedJob:
    id: str 
    owner_id: str 
    status: JobStatus 
    result: Optional[JobResult] 
    pushed_at: datetime 
    shifted_at: Optional[datetime] 
    completed_at: Optional[datetime] 
    retries: int 
    error: Optional[str]
    items: list[JobItem]
