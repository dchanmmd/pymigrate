from sqlalchemy import and_, column, select
from sqlalchemy.orm import Session
from app.model.item_result import ItemResult
from app.model.transfer_job_item import TransferJobItem

class TransferJobItemRepository:
    pg: Session

    def __init__(self, pg: Session):
        self.pg = pg

    def fetch_by_job(self, job_id: str) -> list[TransferJobItem]:
        stmt = (
            select(TransferJobItem)
            .where(
                TransferJobItem.result != ItemResult.Success,
                TransferJobItem.job_id == job_id
            )
        )
        return list(self.pg.scalars(stmt).all())

    def fetch_by_batch(self, job_ids: list[str]) -> list[TransferJobItem]:
        stmt = (
            select(TransferJobItem)
            .where(
                TransferJobItem.result != ItemResult.Success,
                TransferJobItem.job_id.in_(job_ids)
            )
        )
        return list(self.pg.scalars(stmt).all())
