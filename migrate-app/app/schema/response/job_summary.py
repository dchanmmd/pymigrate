from typing import Optional
from pydantic import BaseModel
from app.model.job_status import JobStatus
from app.model.item_result import ItemResult
from app.schema.response.item_status import ItemStatus
from datetime import datetime

class JobSummary(BaseModel):
    job_id: str
    status: JobStatus
    pushed_at: datetime
    completed_at: Optional[datetime]
    recount: dict[ItemResult, int]
    items: list[ItemStatus]
