from sqlalchemy.orm import Session
from app.db.session import get_my_session
from app.repository.inventory_repository import InventoryRepository

class Extractor:
    __my: Session
    __repository: InventoryRepository

    def __init__(self):
        self.__my = get_my_session()
        self.__repository = InventoryRepository(self.__my)
    
    def __enter__(self) -> 'Extractor':
        return self
    
    def __exit__(self, *args) -> None:
        self.__my.close()

    def extract():
        pass

