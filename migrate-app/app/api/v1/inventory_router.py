from typing import Annotated, Optional
from fastapi import APIRouter, Depends

from app.db.session import RequiresRDS
from app.model.inventory_details import InventoryDetails
from app.schema.response.item_response import ItemResponse
from app.schema.response.list_response import ListResponse
from app.service.inventory_service import InventoryService

def __get_service(rds: RequiresRDS):
    return InventoryService(rds)

RequiresInventoryService = Annotated[InventoryService, Depends(__get_service)]

router = APIRouter(prefix='/inventory')

@router.get('/{branch_id}', response_model=ListResponse[InventoryDetails])
def get_item_list(
    service: RequiresInventoryService,
    branch_id: str, 
    page: int = 1, 
    query: Optional[str] = None
):
    result = service.get_items_by_branch(branch_id, 10, page, query)
    count = service.get_count_by_branch(branch_id)
    return ListResponse(
        success=True, 
        message='Se obtuvieron las filas con éxito', 
        data=result, 
        metadata={ 'count': count }
    )

@router.get('/{branch_id}/{item_id}', response_model=ItemResponse[InventoryDetails])
def get_single_item(
    service: RequiresInventoryService,
    branch_id: str, 
    item_id: str
):
    result = service.get_item_by_id(branch_id, item_id)
    return ItemResponse(success=True, message='Se obtuvo el registro con éxito', data=result)