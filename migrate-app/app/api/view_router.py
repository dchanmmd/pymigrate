from app.core.templating import templates
from app.service.branch_service import get_branch_list
from app.service.inventory_service import get_inventory_list
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse

router = APIRouter()

@router.get('/')
def go_to_branches():
    return RedirectResponse(url='/branches')

@router.get('/branches', response_class=HTMLResponse)
def show_branches(request: Request):
    branches = get_branch_list()
    return templates.TemplateResponse(
        request, 
        name='views/branches/index.html', 
        context={ 
            'branches': branches 
        }
    )

@router.get('/branches/{id}/inventory', response_class=HTMLResponse)
def show_branch_inventory(request: Request):
    inventory = get_inventory_list()
    return templates.TemplateResponse(
        request, 
        name='views/branches/{id}/inventory/index.html', 
        context={ 
            'inventory': inventory, 
            'start': 1, 
            'end': 10, 
            'count': 200 
        }
    )
