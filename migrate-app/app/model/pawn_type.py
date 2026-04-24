from datetime import datetime
from app.db.metadata import rds_metadata
from sqlmodel import Field, SQLModel

class PawnType(SQLModel, table=True):
    metadata = rds_metadata
    __tablename__ = 'app_tipoempeno'
    
    idTipoEmpeno: int = Field(primary_key=True)
    nombreTipoEmpeno: str = Field(default=None)
    kilataje: int = Field(default=None)
    pesoTipo: int = Field(default=None)
    ordenamiento: int = Field(default=None)
    vencimiento: int = Field(default=None)
    IDOrigen: int = Field(default=None)
    fecha: datetime = Field(default=None)
    actualizar: int = Field(default=None)
    estado: int = Field(default=None)
    created_at: datetime = Field(default=None)
    updated_at: datetime = Field(default=None)