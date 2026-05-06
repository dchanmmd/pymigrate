from dataclasses import dataclass
from app.model.branch import Branch
from app.model.carat_rating import CaratRating
from app.model.inventory_entry import InventoryEntry
from app.model.pawn_type import PawnType

@dataclass
class JoinedItem:
    entry: InventoryEntry
    branch: Branch
    pawn_type: PawnType
    carat_rating: CaratRating