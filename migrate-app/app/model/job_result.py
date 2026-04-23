from enum import Enum

class JobResult(str, Enum):
    Success = 'éxito'
    PartialSuccess = 'éxito parcial'
    Failure = 'fracaso'