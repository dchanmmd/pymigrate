from app.core.templating import templates
from app.schema.request.transfer_request import TransferRequest
from app.service.inventory_service import get_inventory_list
from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse

router = APIRouter(prefix='/inventory')

@router.get('/{branch_id}/rows', response_class=HTMLResponse)
def get_item_list(request: Request, branch_id: str, page: int = 1, query: str = None):
    print({ 'branch_id': branch_id, 'page': page, 'query': query })
    inventory, last = get_inventory_list(branch_id, page, 10, query)
    
    response = templates.TemplateResponse(request, name='partials/_inv-rows.html', context={ 'inventory': inventory });
    response.headers['X-Is-Last-Page'] = str(last).lower()
    return response

@router.get('/{branch_id}/rows/{item_id}', response_class=HTMLResponse)
def get_item_details(request: Request, branch_id: str, item_id: str):
    print({ 'branch_id': branch_id, 'item_id': item_id})
    item, _ = get_inventory_list(branch_id, 1, 10, None)
    return templates.TemplateResponse(request, name='partials/_item-details.html', context={ 'item': item[0] })

@router.post('/transfer', status_code=202)
def register_transfer_job(body: TransferRequest):
    print(body.__dict__)
    return
