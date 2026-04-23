from pydantic import BaseModel

class ItemStatus(BaseModel):
    item_id: str
    row_id: str
    status: str