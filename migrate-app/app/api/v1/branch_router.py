from typing import Annotated
from app.model.simple_branch import SimpleBranch
from app.schema.response.item_response import ItemResponse
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

@router.get('/{branch_id}', response_model=ItemResponse[SimpleBranch])
def by_id(service: RequiresBranchService, branch_id: int):
    branch = service.get_by_id(branch_id)
    return ItemResponse(success=True, message="Se encontró la sucursal exitosamente", data=branch)