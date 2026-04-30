from app.model.sql.item_result import ItemResult
from dataclasses import dataclass

@dataclass
class JobItem:
    id: str 
    job_id: str 
    row_id: str 
    result: ItemResult 
