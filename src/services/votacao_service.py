from src.domains.comprovante_voto import ComprovanteVoto
from src.repositories.voto_repository import VotoRepository
from src.protos import eleicao_pb2, eleicao_pb2_grpc, candidato_pb2, candidato_pb2_grpc
import hashlib
import hmac
import grpc

repository = VotoRepository()
class VotacaoService:
    def votar(self, voto) -> ComprovanteVoto:
        voto.validar_voto()
        voto.hash_voto = voto.gerar_hash()
        voto_salvo = repository.salvar_voto(voto)
        comprovante_voto = ComprovanteVoto(voto_salvo)
        comprovante_voto.validar_comprovante_voto()
        return comprovante_voto.gerar_comprovante_voto()
        
    def get_voto_existente(self, id_eleicao, id_eleitor):
        return repository.get_voto_eleitor_em_eleicao(id_eleitor, id_eleicao)
    
    def get_eleicao_ativa(self, id_eleicao):
        eleicao_channel = grpc.insecure_channel('localhost:50051')
        eleicao_stub = eleicao_pb2_grpc.EleicaoServiceStub(eleicao_channel)
        eleicao = eleicao_stub.GetEleicao(eleicao_pb2.GetEleicaoRequest(id=id_eleicao))
        if not eleicao or eleicao.status != 'EM ANDAMENTO':
            return None
        return eleicao
    
    def get_candidato_valido(self, id_candidato):
        candidato_channel = grpc.insecure_channel('localhost:50051')
        candidato_stub = candidato_pb2_grpc.CandidatoServiceStub(candidato_channel)
        candidato = candidato_stub.GetCandidato(candidato_pb2.GetCandidatoRequest(id=id_candidato))
        return True if candidato else False
        
    def get_voto_valido(self, id_voto):
        voto = repository.get_voto(id_voto)
        if not voto:
            return False, "Voto não encontrado"
        voto_hash = hmac.new(f"ro6votqwe9rtyi@lpnthe9end1ck".encode(), f"{voto.id_voto}|{voto.id_eleicao}|{voto.id_candidato}".encode(), hashlib.sha256).hexdigest()
        if voto.hash_voto != voto_hash:   
            return False, "Voto inválido"
        return True, "Voto válido"
    
    def get_eleicao_votos(self, id_eleicao):
        return repository.get_votos_por_eleicao(id_eleicao)
        