from enum import StrEnum

class JobStatus(StrEnum):
    Pending = 'pendiente'
    Processing = 'en proceso'
    Completed = 'completado'