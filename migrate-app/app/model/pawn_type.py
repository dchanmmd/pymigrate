from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.mysql import MySQL

class PawnType(MySQL):
    __tablename__ = 'app_tipoempeno'
    
    idTipoEmpeno: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    nombreTipoEmpeno: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    kilataje: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    pesoTipo: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    ordenamiento: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    vencimiento: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    IDOrigen: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    fecha: Mapped[Optional[datetime]] = mapped_column()
    actualizar: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    estado: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    created_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)