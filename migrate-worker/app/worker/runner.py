from app.config.app_environment import env
from app.db.session import get_pg_session
from app.repository.transfer_job_item_repository import TransferJobItemRepository
from app.repository.transfer_job_repository import TransferJobRepository
from collections import defaultdict

def run():
    batch_limit = env.BATCH_LIMIT or 10

    while True:
        with get_pg_session() as pg:
            job_repo = TransferJobRepository(pg)
            item_repo = TransferJobItemRepository(pg)

            jobs = job_repo.claim_pending(batch_limit)

            if not jobs:
                break

            job_ids = [j.job_id for j in jobs]
            items = item_repo.fetch_by_batch(job_ids)

            items_by_job = defaultdict(list)

            for item in items:
                items_by_job[item.job_id].append(item)

            try:
                for job in jobs:
                    job_items = items_by_job[job.job_id]
                    job_items # work()
            except Exception:
                job_repo.mark_failed_or_retry(job_ids)
                raise

            if len(jobs) < batch_limit:
                break