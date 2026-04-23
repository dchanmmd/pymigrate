from enum import Enum

class JobStatus(str, Enum):
    Pending = 'pendiente'
    Processing = 'en proceso'
    Completed = 'completado'