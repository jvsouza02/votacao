from datetime import datetime
from uuid import uuid4
from src.services.votacao_service import VotacaoService
import hashlib
import hmac

votacao_service = VotacaoService()

class Voto:
    def __init__(self, id_eleicao: str, id_eleitor: int, id_candidato: str):
        self.id_voto = uuid4()
        self.id_eleicao = id_eleicao
        self.id_eleitor = id_eleitor
        self.id_candidato = id_candidato
        self.hash_voto = None
        self.data_voto = datetime.now()

    def gerar_hash(self):
        self.hash_voto = hmac.new(f"ro6votqwe9rtyi@lpnthe9end1ck".encode(), f"{self.id_voto}|{self.id_eleicao}|{self.id_candidato}".encode(), hashlib.sha256).hexdigest()
        return self.hash_voto
    
    def validar_voto_unico(self):
        voto_existente = votacao_service.get_voto_existente(self.id_eleicao, self.id_eleitor)
        if voto_existente:
            raise ValueError("Eleitor já votou nesta eleição.")
        return True
    
    def validar_eleicao_ativa(self):
        eleicao = votacao_service.get_eleicao_ativa(self.id_eleicao)
        if not eleicao:
            raise ValueError("A eleição não está ativa.")
        return True
    
    def validar_candidato(self):
        candidato = votacao_service.get_candidato_valido(self.id_candidato)
        if not candidato:
            raise ValueError("Candidato inválido para esta eleição.")
        return True
    
    def validar_integridade_voto(self):
        voto_valido = votacao_service.get_voto_valido(self.id_voto)
        if not voto_valido:
            raise ValueError("Voto inválido.")
        return True
    
    def validar_voto(self):
        self.validar_voto_unico()
        # self.validar_eleicao_ativa()
        # self.validar_candidato()
        return True
    
    
        
    


    
    