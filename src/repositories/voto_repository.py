from src.models.voto_model import Voto, RegistroVotante
from sqlalchemy import select
from sqlalchemy.orm import Session
from config.database import get_db

class VotoRepository:
    def __init__(self, db: Session = next(get_db())):
        self.db = db

    def salvar_voto(self, voto):
        voto_salvo = Voto(id_voto = voto.id_voto, id_eleicao = voto.id_eleicao, id_candidato = voto.id_candidato, hash_voto = voto.hash_voto, data_voto = voto.data_voto)
        registro_votante = RegistroVotante(id_eleicao=voto.id_eleicao, id_eleitor=voto.id_eleitor)
        try:
            self.db.add(voto_salvo)
            self.db.add(registro_votante)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        return voto
    
    def get_voto(self, id_voto):
        try:
            return self.db.execute(select(Voto).where(Voto.id_voto == id_voto)).scalars().first()
        except Exception as e:
            raise e
    
    def get_voto_eleitor_em_eleicao(self, id_eleitor, id_eleicao):
        try:
            return self.db.execute(
                select(RegistroVotante).where(
                    RegistroVotante.id_eleitor == id_eleitor,
                    RegistroVotante.id_eleicao == id_eleicao
                ).scalars().first()
            )
        except Exception as e:
            raise e
    
    def get_votos_por_eleicao(self, id_eleicao):
        try:
            return self.db.execute(
                select(Voto).where(Voto.id_eleicao == id_eleicao)
            ).scalars().all()
        except Exception as e:
            raise e
