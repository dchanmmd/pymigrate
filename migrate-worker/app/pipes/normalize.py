from app.types.joined_item import JoinedItem
from app.types.normalized_item import NormalizedItem

def trimstr(text: str) -> str:
    return ' '.join(text.split())

def normalize(item: JoinedItem) -> NormalizedItem:
    pass