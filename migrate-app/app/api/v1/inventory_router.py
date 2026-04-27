from typing import Optional

from fastapi import APIRouter

router = APIRouter(prefix='/inventory')

@router.get('/{branch_id}')
def get_item_list(branch_id: str, page: int = 1, query: Optional[str] = None):
    print({ 'branch_id': branch_id, 'page': page, 'query': query })
    return

@router.get('/{branch_id}/{item_id}')
def get_single_item(branch_id: str, item_id: str):
    print({ 'branch_id': branch_id, 'item_id': item_id })
    return