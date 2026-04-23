from app.schema.response.item_status import ItemStatus
from datetime import datetime
from pydantic import BaseModel

class JobStatusResponse(BaseModel):
    job_id: str
    status: str
    completed_at: datetime | None
    items: list[ItemStatus]
