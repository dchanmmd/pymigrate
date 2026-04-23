from app.db.metadata import rds_metadata
from datetime import datetime
from sqlmodel import SQLModel, Field

class Branch(SQLModel, table=True):
    metadata = rds_metadata
    __tablename__ = 'app_sucursales'
    id: int = Field(primary_key=True)
    idTabla: int
    siglas: str
    clave: int
    ordenamiento: int
    ip: str
    meraki: str
    razonSocial: str
    nombreComercial: str
    alias: str
    rfc: str
    direccion: str
    ciudad: str
    municipio: str
    idDistrito: int
    idCorregimiento: int
    telefono: str
    cp: int
    region: str
    zona: str
    provincia: str
    latitud: str
    longitud: str
    horarioEmpenos: str
    horarioRetiros: str
    horarioWU: str
    horarioVentas: str
    fluyapp: str
    googleMaps: str
    activa: int
    cuenta: str
    IDOrigen: int
    Actualizar: int
    ElConix_Companie: str
    ElConix_CentroCosto: str
    rucFiscal: str
    dvFiscal: str
    grupo: int
    visible: int
    migrada: datetime
    estado: int
    eliminado: int
    doc_jefe_unidad: str
    created_at: datetime
    updated_at: datetime
