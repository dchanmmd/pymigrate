from typing import Annotated
from app.model.simple_branch import SimpleBranch
from app.schema.response.list_response import ListResponse
from app.db.session import RequiresRDS
from app.service.branch_service import BranchService
from fastapi import APIRouter, Depends


def __get_service(rds: RequiresRDS):
    return BranchService(rds)

RequiresBranchService = Annotated[BranchService, Depends(__get_service)]

router = APIRouter(prefix='/branches')

@router.get('/', response_model=ListResponse[SimpleBranch])
def all_branches(service: RequiresBranchService):
    branches = service.get_branch_list()
    return ListResponse(success=True, message="Se encontraron las sucursales exitosamente", data=branches)