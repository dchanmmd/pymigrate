from app.db.session import RequiresRDS
from app.core.templating import templates
from app.service.branch_service import get_branch_list
from app.service.inventory_service import get_inventory_list
from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse

router = APIRouter()

@router.get('/')
def go_to_branches():
    return RedirectResponse(url='/branches')

@router.get('/login', response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse(
        request, 
        name='views/login/index.html', 
    )


@router.get('/branches', response_class=HTMLResponse)
def show_branches(request: Request, rds: RequiresRDS):
    branches = get_branch_list(rds)
    return templates.TemplateResponse(
        request, 
        name='views/branches/index.html', 
        context={ 
            'branches': branches 
        }
    )

@router.get('/branches/{branch_id}/inventory', response_class=HTMLResponse)
def show_branch_inventory(request: Request, branch_id: str):
    inventory, last = get_inventory_list(branch_id, 1, 10, None)
    response = templates.TemplateResponse(
        request, 
        name='views/branches/{id}/inventory/index.html', 
        context={ 
            'inventory': inventory, 
            'start': 1, 
            'end': 10, 
            'count': 200 
        }
    )
    response.headers['X-Is-Last-Page'] = str(last).lower()
    return response


