from app.db.session import RequiresRDS
from app.model.branch import Branch
from app.model.simple_branch import SimpleBranch
from sqlmodel import Session, select

mmd_si = 3

def get_branch_list(rds: Session):
    query = select(Branch.id, Branch.nombreComercial).where(Branch.grupo == mmd_si)
    result = rds.exec(query).all()
    print([r for r in result])
    return [SimpleBranch(id=str(r[0]), name=str(r[1])) for r in result]