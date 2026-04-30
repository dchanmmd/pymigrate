from abc import ABC

class BaseModel(ABC):
    """
    Utilizará las anotaciones de las clases que
    la hereden para crear un diccionario utilizable
    como objeto para Model.write en Odoo
    """
    pass