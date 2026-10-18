from sqlalchemy import Column, Integer, Numeric, Boolean, String, TIMESTAMP
from sqlalchemy.sql import text
from database import Base

DEFAULT_TIMESTAMP = text('now()')

class promocao_steam(Base):
  __tablename__ = "promocao_steam"
  id = Column(Integer, primary_key=True, nullable=False)
  nome = Column(String, nullable=True)
  desconto = Column(String, nullable=True)
  preco_original = Column(Numeric(10, 2), nullable=True)
  preco_final = Column(Numeric(10, 2), nullable=True)
  link = Column(String, nullable=True)
  imagem = Column(String, nullable=True)
  publicado = Column(Boolean, server_default='True', nullable=False)
  created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=DEFAULT_TIMESTAMP)