import re
from app.core.category_resolver import ResultTuple, procedural_resolver
from app.model.inventory_details import InventoryDetails
from app.model.inventory_entry import InventoryEntry as IE
from app.model.branch import Branch as Br
from app.model.pawn_type import PawnType as PT
from app.model.carat_rating import CaratRating as CR
from typing import Optional
from sqlmodel import Session, func, select, and_

class InventoryService:
    rds: Session

    def __query(self, branch_id: str, barcode: Optional[str] = None):
        conditions = [
            c
            for c in [
                IE.cantidad >= 1,
                IE.sucursalDestino == branch_id,
                (IE.codigo == barcode) if barcode is not None else None,
            ]
            if c is not None
        ]

        return (
            select(
                IE.codigo,
                IE.descripcion,
                IE.pesoDotacion,
                IE.precio,
                IE.costo,
                IE.observaciones,
                IE.idEmpeno,
                IE.pesoPiedras,
                IE.marca,
                IE.modelo,
                IE.serie,
                CR.nombreKilataje,
                PT.nombreTipoEmpeno,
                Br.nombreComercial,
            )
            .join(Br, IE.sucursalDestino == Br.id)
            .join(PT, IE.tipoDotacion == PT.idTipoEmpeno)
            .join(CR, IE.kilates == CR.Clave)
            .where(and_(*conditions))
            .order_by(IE.id_entrada_inventario.desc())
        )
    
    def __count(self, branch_id: str):
        return (
            select(func.count())
            .select_from(IE)
            .join(Br, IE.sucursalDestino == Br.id)
            .join(PT, IE.tipoDotacion == PT.idTipoEmpeno)
            .join(CR, IE.kilates == CR.Clave)
            .where(and_(IE.cantidad >= 1, IE.sucursalDestino == branch_id))
        )

    def __details_resolve_name(self, row: ResultTuple) -> str | None:
        description = row[1]
        carat_rating = row[11]
        weight = row[2]
        pawn_type = row[12]
        observations = row[5]
        barcode = row[0]

        return (
            ' '.join(w for w in [
                    ' '.join([w for w in [
                                description.strip().title(),
                                carat_rating.strip(),
                                f'{weight}grs.' if weight > 0 else None,
                            ] if bool(w)]),
                    '-'.join([w.strip() for w in [
                        pawn_type, 
                        observations, 
                        barcode
                        ] if w]).lower(),
                ] if w) or None
        )
    
    def __details_resolve_category(self, row: ResultTuple) -> str:
        return procedural_resolver(row)

    def __to_details(self, row: ResultTuple) -> InventoryDetails:
        return InventoryDetails(
            internal_ref=row[0],
            barcode=row[0],
            name=self.__details_resolve_name(row),
            uom='Unidades',
            purchase_uom='Unidades',
            weight=row[2],
            can_be_sold=True,
            can_be_bought=False,
            product_type='Producto almacenable',
            provider_tax='ITBMS',
            customer_tax='ITBMS',
            tags='Lógica de etiquetas',
            retail_price=row[3],
            cost=row[4],
            observations=row[5],
            pawn_no=row[6],
            stone_weight=row[7],
            brand=row[8],
            model=row[9],
            series=row[10],
            branch = re.sub(r"\s+", ' ', row[13].replace('MASMEDAN', '')).strip(),
            product_category=self.__details_resolve_category(row)
        )

    def __init__(self, rds: Session):
        self.rds = rds

    def get_by_barcode(self, branch_id: str, query: str):
        stmt = self.__query(branch_id, query)
        result = self.rds.exec(stmt).one()
        return self.__to_details(result)