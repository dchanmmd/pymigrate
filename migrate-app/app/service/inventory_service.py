import re
from typing import Optional
from sqlalchemy import select
from sqlalchemy.engine import Row
from sqlalchemy.orm import Session
from app.core.category_resolver import procedural_resolver
from app.model.inventory_details import InventoryDetails
from app.model.inventory_entry import InventoryEntry as IE
from app.model.branch import Branch as Br
from app.model.pawn_type import PawnType as PT
from app.model.carat_rating import CaratRating as CR

class InventoryService:
    my: Session

    def __init__(self, my: Session):
        self.my = my

    def __stmt(self, branch_id: str, barcode: Optional[str] = None):
        conditions = [c for c in [
            IE.cantidad >= 1,
            Br.id.in_([826, 832, 840, 841, 852, 857, 869, 876, 885, 888, 891]),
            IE.sucursalDestino >= 803,
            IE.sucursalDestino == branch_id,
            (IE.codigo == barcode) if barcode is not None else None,
        ] if c is not None]

        return (
            select(
                IE.codigo.label('barcode'),
                IE.descripcion.label('description'),
                IE.pesoDotacion.label('weight'),
                IE.precio.label('retail_price'),
                IE.costo.label('cost'),
                IE.observaciones.label('observations'),
                IE.idEmpeno.label('pawn_no'),
                IE.pesoPiedras.label('stone_weight'),
                IE.marca.label('brand'),
                IE.modelo.label('model'),
                IE.serie.label('series'),
                CR.nombreKilataje.label('carat_rating'),
                PT.nombreTipoEmpeno.label('pawn_type'),
                Br.nombreComercial.label('branch'),
            )
            .join(Br, IE.sucursalDestino == Br.id)
            .join(PT, IE.tipoDotacion == PT.idTipoEmpeno)
            .join(CR, IE.kilates == CR.Clave)
            .where(*conditions)
            .order_by(IE.id_entrada_inventario.desc())
        )
    
    def __details_resolve_name(self, row: Row) -> str | None:
        description = row.description
        carat_rating = row.carat_rating
        weight = row.weight
        pawn_type = row.pawn_type
        observations = row.observations
        barcode = row.barcode

        main = ' '.join(
            w for w in [
                (description.strip().title() if description else None),
                (carat_rating.strip() if carat_rating else None),
                (f'{weight}grs.' if weight and weight > 0 else None),
            ]
            if w
        )

        suffix = '-'.join(
            w.strip() for w in [pawn_type, observations, barcode] if w
        ).lower()

        result = ' '.join(w for w in [main, suffix] if w)
        return result or None
    
    @staticmethod
    def __details_resolve_category(row: Row) -> str:
        return procedural_resolver(row)
    
    @staticmethod
    def __details_resolve_branch(branch: Optional[str]) -> str:
        return '' if not branch else ' '.join(branch.replace('MASMEDAN', '').split())
    

    def __to_details(self, row: Row) -> InventoryDetails:
        return InventoryDetails(
            internal_ref=row.barcode,
            barcode=row.barcode,
            name=self.__details_resolve_name(row),
            description=row.description,
            uom='Unidades',
            purchase_uom='Unidades',
            weight=row.weight,
            carat_rating=row.carat_rating,
            can_be_sold=True,
            can_be_bought=False,
            product_type='Producto almacenable',
            provider_tax='ITBMS',
            customer_tax='ITBMS',
            tags='Lógica de etiquetas',
            retail_price=row.retail_price,
            cost=row.cost,
            observations=row.observations,
            pawn_no=row.pawn_no,
            stone_weight=row.stone_weight,
            brand=row.brand,
            model=row.model,
            series=row.series,
            branch=self.__details_resolve_branch(row.branch),
            product_category=self.__details_resolve_category(row),
        )
      
    def get_by_barcode(self, branch_id: str, query: str) -> InventoryDetails | None:
        stmt = self.__stmt(branch_id, query)
        result = self.my.execute(stmt).first()
        if result is None:
            return None
        return self.__to_details(result) 