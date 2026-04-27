from app.db.metadata import pg_metadata
from typing import Optional

from sqlmodel import Field, SQLModel

class CategoryMap(SQLModel, table=True):
    __tablename__ = 'odoo_product_category_map'
    metadata = pg_metadata

    id: int = Field(primary_key=True)
    category: str = Field(nullable=False)
    kilataje: Optional[str] = Field(default=None)
    palabra_clave: str = Field(nullable=False)
    categoria_odoo: str = Field(nullable=False)