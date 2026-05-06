from typing import Annotated, Optional
from fastapi import APIRouter, Depends, HTTPException

from app.db.session import RequiresMySQL
from app.model.inventory_details import InventoryDetails
from app.schema.response.item_response import ItemResponse
from app.schema.response.list_response import ListResponse
from app.service.inventory_service import InventoryService

def __get_service(rds: RequiresMySQL):
    return InventoryService(rds)

RequiresInventoryService = Annotated[InventoryService, Depends(__get_service)]

router = APIRouter(prefix='/inventory')

@router.get('/{branch_id}', response_model=ItemResponse[InventoryDetails])
def search_barcode(
    service: RequiresInventoryService,
    branch_id: str,
    query: str
):
    details = service.get_by_barcode(branch_id, query.strip())
    if details is None:
        raise HTTPException(404, detail='No se encontraron registros para este código de barra')
    return ItemResponse(success=True, message='Se obtuvo el registro con éxito', data=details)

@router.get('/{branch_id}/{barcode}', response_model=ItemResponse[InventoryDetails])
def by_barcode(
    service: RequiresInventoryService,
    branch_id: str,
    barcode: str
):
    details = service.get_by_barcode(branch_id, barcode)
    if details is None:
        raise HTTPException(404, detail='No se encontraron registros para este código de barra')
    return ItemResponse(success=True, message='Se obtuvo el registro con éxito', data=details)

