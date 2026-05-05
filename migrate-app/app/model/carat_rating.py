from datetime import datetime
from typing import Optional
from sqlalchemy import Float, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.db.mysql import MySQL

class CaratRating(MySQL):
    __tablename__ = 'app_kilatajes'

    idKilataje: Mapped[int] = mapped_column(Integer, primary_key=True)
    Clave: Mapped[Optional[int]] = mapped_column(Integer, default=None)
    nombreKilataje: Mapped[Optional[str]] = mapped_column(String, default=None)
    idTipoEmpeno: Mapped[Optional[int]] = mapped_column(Integer, default=None)
    IDTablaTipo: Mapped[Optional[int]] = mapped_column(Integer, default=None)
    valorxGramo: Mapped[Optional[float]] = mapped_column(Float, default=None)
    Ordenamiento: Mapped[Optional[int]] = mapped_column(Integer, default=None)
    IDOrigen: Mapped[Optional[int]] = mapped_column(Integer, default=None)
    FechaModificacion: Mapped[Optional[datetime]] = mapped_column(DateTime, default=None)
    Actualizar: Mapped[Optional[int]] = mapped_column(Integer, default=None)
    estado: Mapped[Optional[int]] = mapped_column(Integer, default=None)
    created_at: Mapped[Optional[datetime]] = mapped_column(DateTime, default=None)
    updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime, default=None)