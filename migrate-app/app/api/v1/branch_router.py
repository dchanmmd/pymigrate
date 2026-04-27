from fastapi import APIRouter

router = APIRouter(prefix='/branches')

@router.get('/')
def all_branches():
    pass