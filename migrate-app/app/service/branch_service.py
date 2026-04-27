from sqlmodel import Session, select

from app.model.branch import Branch
from app.model.simple_branch import SimpleBranch

class BranchService:
    __mmd_si: int = 3
    rds: Session

    def __init__(self, rds: Session):
        self.rds = rds

    def get_branch_list(self):
        query = select(Branch.id, Branch.nombreComercial).where(Branch.grupo == self.__mmd_si)
        result = self.rds.exec(query).all()
        return [SimpleBranch(id=str(r[0]), name=str(r[1])) for r in result]