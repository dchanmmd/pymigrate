from pydantic import BaseModel

class ListResponse[T](BaseModel):
    success: bool
    message: str
    data: list[T]