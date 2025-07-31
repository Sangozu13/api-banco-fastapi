from pydantic import BaseModel
from typing import Optional, Literal


class Account(BaseModel):
    id: Optional[str] = None
    nombre_titular : str
    numero_cuenta : str
    saldo: int
    tipo_cuenta : str
    is_active: bool = True
    
class UpdateSaldoAccount(BaseModel):
    saldo: int
    operacion: Literal["sumar", "restar"]