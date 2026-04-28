from typing import Any, Optional

from pydantic import BaseModel

class ListResponse[T](BaseModel):
    success: bool
    message: str
    data: list[T]
    metadata: Optional[dict[str, Any]] = None