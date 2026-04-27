from pydantic import BaseModel

from app.model.item_result import ItemResult
from app.schema.response.item_status import ItemStatus
from datetime import datetime

class JobSummary(BaseModel):
    job_id: str
    status: str
    completed_at: datetime | None
    recount: dict[ItemResult, int]
    items: list[ItemStatus]
