from enum import Enum

class ItemResult(str, Enum):
    Pending = 'pendiente'
    Success = 'éxito'
    Failure = 'fracaso'