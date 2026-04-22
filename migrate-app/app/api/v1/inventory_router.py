from app.core.templating import templates
from app.schema.transfer_request import TransferRequest
from app.service.inventory_service import get_inventory_list
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter(prefix='/inventory')

@router.get('/{branch_id}/rows', response_class=HTMLResponse)
def get_item_list(request: Request, branch_id: str, page: int = 1, query: str = None):
    # Ensure query and path params are passing correctly
    print({ 'branch_id': branch_id, 'page': page, 'query': query })

    items = get_inventory_list()
    return templates.TemplateResponse(request, name='partials/_inv-rows.html', context={ 'inventory': items });

@router.get('/{branch_id}/rows/{item_id}', response_class=HTMLResponse)
def get_item_details(request: Request, branch_id: str, item_id: str):
    # Ensure path params are passing correctly
    print({ 'branch_id': branch_id, 'item_id': item_id})
    item = get_inventory_list()[0]
    return templates.TemplateResponse(request, name='partials/_item-details.html', context={ 'item': item })

@router.post('/transfer', status_code=202)
def register_transfer_job(body: TransferRequest):
    print(body.__dict__)
    return
