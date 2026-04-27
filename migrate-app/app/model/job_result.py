from enum import StrEnum

class JobResult(StrEnum):
    Success = 'éxito'
    PartialSuccess = 'éxito parcial'
    Failure = 'fracaso'