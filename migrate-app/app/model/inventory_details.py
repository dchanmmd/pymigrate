from typing import Optional

from sqlmodel import SQLModel

class InventoryDetails(SQLModel):
    internal_ref: Optional[str]
    barcode: Optional[str]
    name: Optional[str]
    uom: Optional[str]
    purchase_uom: Optional[str]
    weight: Optional[float]
    can_be_sold: Optional[bool] # Literal[True]
    can_be_bought: Optional[bool] # Literal[False]
    product_type: Optional[str] # Literal['Producto Almacenable']
    provider_tax: Optional[str] # Literal['ITBMS']
    customer_tax: Optional[str] # Literal['ITBMS']
    tags: Optional[str] # Literal['Lógica de etiquetas']
    retail_price: Optional[float]
    cost: Optional[float]
    observations: Optional[str]
    pawn_no: Optional[str]
    stone_weight: Optional[float]
    brand: Optional[str]
    model: Optional[str]
    series: Optional[str]
    branch: Optional[str]
    product_category: Optional[str]