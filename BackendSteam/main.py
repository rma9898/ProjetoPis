from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, status, Depends, HTTPException, Response
from schemas import PromocaoSteam, PromocaoSteamResponse
import models
from database import engine, get_db
from sqlalchemy.orm import Session
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['http://localhost:3000']

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)

@app.post("/promocoes", status_code=status.HTTP_201_CREATED)
async def criar_promocao(promocao: PromocaoSteam, db: Session = Depends(get_db)):
  nova_promocao = models.promocao_steam(**promocao.model_dump())
  db.add(nova_promocao)
  db.commit()
  db.refresh(nova_promocao)
  print(promocao)
  return {"PromocaoSteam": nova_promocao}

@app.get("/promocoes", response_model=List[PromocaoSteamResponse], status_code=status.HTTP_200_OK)
async def buscar_promocoes(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
  promocoes = db.query(models.promocao_steam).offset(skip).limit(limit).all()
  return promocoes

@app.put("/promocoes/{promocao_id}", response_model=PromocaoSteamResponse, status_code=status.HTTP_200_OK)
async def atualizar_promocao(promocao_id: int, promocao: PromocaoSteam, db: Session = Depends(get_db)):
  promocao_query = db.query(models.promocao_steam).filter(models.promocao_steam.id == promocao_id)
  promocao_existente = promocao_query.first()
  
  if promocao_existente is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promoção não encontrada")
      
  promocao_query.update(promocao.model_dump(), synchronize_session=False)
  db.commit()
  return promocao_query.first()

@app.delete("/promocoes/{promocao_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remover_promocao(promocao_id: int, db: Session = Depends(get_db)):
  promocao_query = db.query(models.promocao_steam).filter(models.promocao_steam.id == promocao_id)
  
  if promocao_query.first() is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promoção não encontrada")
      
  promocao_query.delete(synchronize_session=False)
  db.commit()
  return Response(status_code=status.HTTP_204_NO_CONTENT)