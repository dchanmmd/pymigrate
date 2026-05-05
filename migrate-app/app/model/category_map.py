from typing import Optional
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.postgres import Postgres

class CategoryMap(Postgres):
    __tablename__ = 'odoo_product_category_map'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category: Mapped[str] = mapped_column(String, nullable=False)
    kilataje: Mapped[Optional[str]] = mapped_column(String, default=None)
    palabra_clave: Mapped[str] = mapped_column(String, nullable=False)
    categoria_odoo: Mapped[str] = mapped_column(String, nullable=False)