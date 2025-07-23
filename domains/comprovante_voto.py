from datetime import datetime
from services.comprovante_voto_service import ComprovanteVotacaoService

comprovante_votacao_service = ComprovanteVotacaoService()
class ComprovanteVoto:
    def __init__(self, voto):
        self.id_comprovante_voto = voto.id_voto
        self.id_eleicao = voto.id_eleicao
        self.data_voto = voto.data_voto
        self.data_geracao = datetime.now()

    def gerar_comprovante_voto(self) -> dict:
        return {"id_comprovante_voto": self.id_comprovante_voto, "id_eleicao": self.id_eleicao, "data_voto": str(self.data_voto), "data_geracao": str(self.data_geracao)}
        
    
    def validar_comprovante_para_voto_valido(self):
        if not comprovante_votacao_service.get_voto_valido(self.id_comprovante_voto):
            raise ValueError("Voto inválido. Não é possível gerar comprovante.")
        return True
    
    def validar_comprovante_nao_expoe_voto(self, comprovante):
        if not comprovante_votacao_service.get_comprovante_voto_valido(comprovante):
            raise ValueError('O comprovante expõe o voto.')
        return True
    
    def validar_comprovante_voto_unico(self, id_comprovante_voto):
        if not comprovante_votacao_service.get_comprovante_voto_unico(id_comprovante_voto):
            raise ValueError("Comprovante de Voto já utilizado.")
        return True
    
    def validar_comprovante_voto(self):
        # self.validar_comprovante_para_voto_valido()
        # self.validar_comprovante_nao_expoe_voto(self.comprovante)
        # self.validar_comprovante_voto_unico(self.id_comprovante_voto)
        return True
    


    