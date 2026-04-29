from app.model.item_result import ItemResult
from pydantic import BaseModel

class ItemStatus(BaseModel):
    item_id: str
    row_id: str
    result: ItemResult