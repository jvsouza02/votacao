import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, DateTime, UniqueConstraint
from datetime import datetime

Base = declarative_base()

class Voto(Base):
    __tablename__ = 'votos'

    id_voto = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_eleicao = Column(Integer, nullable=False)
    id_candidato = Column(Integer, nullable=False)
    hash_voto = Column(String(64), nullable=False, unique=True)
    data_voto = Column(DateTime, default=datetime.now(), nullable=False)

class RegistroVotante(Base):
    __tablename__ = 'registro_votantes'

    id_registro_voto = Column(Integer, primary_key=True)
    id_eleicao = Column(Integer, nullable=False)
    id_eleitor = Column(Integer, nullable=False)
    data_registro = Column(DateTime, default=datetime.now(), nullable=False)

    __table_args__ = (UniqueConstraint('id_eleitor', 'id_eleicao'),)

