from sqlmodel import Enum

class JobStatus(str, Enum):
    Pending = 'pending'
    Processing = 'processing'
    Success = 'success'
    Failure = 'failure'