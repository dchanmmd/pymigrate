from typing import Any, Optional

from pydantic import BaseModel

class ItemResponse[T](BaseModel):
    success: bool
    message: str
    data: T
    metadata: Optional[dict[str, Any]] = None