from datetime import datetime
from typing import Optional
from app.db.metadata import rds_metadata
from sqlmodel import SQLModel, Field


class CaratRating(SQLModel, table=True):
    metadata = rds_metadata
    __tablename__ = 'app_kilatajes'

    idKilataje: int = Field(primary_key=True)
    Clave: Optional[int] = Field(default=None)
    nombreKilataje: Optional[str] = Field(default=None)
    idTipoEmpeno: Optional[int] = Field(default=None)
    IDTablaTipo: Optional[int] = Field(default=None)
    valorxGramo: Optional[float] = Field(default=None)
    Ordenamiento: Optional[int] = Field(default=None)
    IDOrigen: Optional[int] = Field(default=None)
    FechaModificacion: Optional[datetime] = Field(default=None)
    Actualizar: Optional[int] = Field(default=None)
    estado: Optional[int] = Field(default=None)
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)