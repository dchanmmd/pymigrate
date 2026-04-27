from typing import Optional

from sqlmodel import Session, select

class InventoryService:
    rds: Session

    def __init__(self, rds: Session):
        self.rds = rds
    
    def get_items_by_branch(self, branch_id: str, limit: int, page: int, query: Optional[str] = None):
        offset = max(0, page - 1) * limit
        query = select()
        result = self.rds.exec(query.limit(limit).offset(offset)).all()
        pass

    def get_item_by_id():
        pass