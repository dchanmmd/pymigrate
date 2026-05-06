from typing import Annotated
from app.schema.response.simple_branch import SimpleBranch
from app.schema.response.item_response import ItemResponse
from app.schema.response.list_response import ListResponse
from app.db.session import RequiresMySQL
from app.service.branch_service import BranchService
from fastapi import APIRouter, Depends, HTTPException


def __get_service(rds: RequiresMySQL):
    return BranchService(rds)

RequiresBranchService = Annotated[BranchService, Depends(__get_service)]

router = APIRouter(prefix='/branches')

@router.get('/', response_model=ListResponse[SimpleBranch])
def all_branches(service: RequiresBranchService):
    branches = service.get_list()
    if branches:
        return ListResponse(success=True, message="Se encontraron las sucursales exitosamente", data=branches)
    raise HTTPException(404, detail='No se encontraron sucursales.')

@router.get('/{branch_id}', response_model=ItemResponse[SimpleBranch])
def by_id(service: RequiresBranchService, branch_id: int):
    branch = service.get_by_id(branch_id)
    if branch is not None:
        return ItemResponse(success=True, message="Se encontró la sucursal exitosamente", data=branch)
    raise HTTPException(404, detail='No se encontró la sucursal.')