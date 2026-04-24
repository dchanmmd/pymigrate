from typing import Literal

from sqlmodel import SQLModel

class InventoryDetails(SQLModel):
    internal_ref: str
    barcode: str
    name: str
    uom: str
    purchase_uom: str
    weight: float
    can_be_sold: Literal[True]
    can_be_bought: Literal[False]
    product_type: Literal['Producto Almacenable']
    provider_tax: Literal['ITBMS']
    client_tax: Literal['ITBMS']
    tags: Literal['Lógica de etiquetas']
    sale_price: float
    cost: float
    observations: str
    pawn_no: str
    stone_weight: float
    brand: str
    model: str
    series: str
    branch: str
    product_category: str