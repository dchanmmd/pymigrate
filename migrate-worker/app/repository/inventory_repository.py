from sqlalchemy import select
from sqlalchemy.orm import Session
from app.model.inventory_entry import InventoryEntry as IE
from app.model.branch import Branch as Br
from app.model.carat_rating import CaratRating as CR
from app.model.pawn_type import PawnType as PT
from app.types.joined_item import JoinedItem

type ResultTuple = tuple[IE, Br, PT, CR]

class InventoryRepository:
    my: Session

    def __init__(self, my: Session):
        self.my = my

    @staticmethod
    def __to_joined(row: ResultTuple) -> JoinedItem:
        return JoinedItem(row[0], row[1], row[2], row[2])

    @staticmethod
    def __stmt(*barcodes: str):
        return (
            select(IE, Br, PT, CR)
                .join(Br, IE.sucursalDestino == Br.id)
                .join(PT, IE.tipoDotacion == PT.idTipoEmpeno)
                .join(CR, IE.kilates == CR.Clave)
                .where(
                    IE.cantidad >= 1,
                    Br.id.in_([826, 832, 840, 841, 852, 857, 869, 876, 885, 888, 891]),
                    IE.sucursalDestino >= 803,
                    IE.codigo == barcodes[0] if len(barcodes) == 1 else IE.codigo.in_(barcodes)
                )
        )
    
    def batch_by_barcode(self, barcodes: list[str]) -> list[ResultTuple]:
        return [self.__to_joined(i) for i in self.my.execute(self.__stmt(*barcodes)).all()]

    def get_by_barcode(self, barcode: str) -> ResultTuple | None:
        return self.__to_joined(self.my.execute(self.__stmt(barcode)).first())