from pydantic import BaseModel

class SimpleBranch(BaseModel):
    id: int
    name: str