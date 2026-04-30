from app.db.session import get_pg_session
from app.service.job_service import JobService

def main():
    with get_pg_session() as pg:
        job_service = JobService(pg=pg)
        jobs = job_service.get_earliest_jobs(10)

if __name__ == '__main__':
    main()

