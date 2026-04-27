from pydantic import BaseModel

class ItemResponse[T](BaseModel):
    success: bool
    message: str
    data: T