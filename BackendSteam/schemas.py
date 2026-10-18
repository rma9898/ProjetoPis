from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from typing import Optional
  
class PromocaoSteam(BaseModel):
  nome: str
  desconto: Optional[str] = None
  preco_original: Optional[Decimal] = None
  preco_final: Optional[Decimal] = None
  link: Optional[str] = None
  imagem: Optional[str] = None
  publicado: bool = True

class PromocaoSteamResponse(PromocaoSteam):
  id: int
  model_config = ConfigDict(from_attributes=True)