from pydantic import BaseModel
from app.model.item_result import ItemResult

class ItemStatus(BaseModel):
    item_id: str
    row_id: str
    result: ItemResult