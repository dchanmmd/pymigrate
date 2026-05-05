from sqlalchemy import select
from sqlalchemy.engine import Row
from sqlalchemy.orm import Session
from app.model.branch import Branch
from app.schema.response.simple_branch import SimpleBranch

class BranchService:
    __mmd_si: int = 3
    __select = select(Branch.id.label('id'), Branch.nombreComercial.label('name'))

    my: Session

    def __init__(self, my: Session):
        self.my = my

    @staticmethod
    def __to_simple(row: Row) -> SimpleBranch:
        return SimpleBranch(id=row.id, name=row.name)

    def get_list(self) -> list[SimpleBranch]:
        stmt = self.__select.where(Branch.grupo == self.__mmd_si)
        result = self.my.execute(stmt).all()
        return [self.__to_simple(b) for b in result]
    
    def get_by_id(self, branch_id: int) -> SimpleBranch | None:
        stmt = self.__select.where(Branch.grupo == self.__mmd_si, Branch.id == branch_id)
        result = self.my.execute(stmt).first()
        return self.__to_simple(result) if result else None