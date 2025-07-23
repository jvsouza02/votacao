from repositories.voto_repository import VotoRepository
import hashlib
import hmac

repository = VotoRepository()

class ComprovanteVotacaoService:
    def get_voto_valido(self, id_voto: int):
        voto = repository.get_voto(id_voto)
        if not voto:
            return None
        voto_hash = hmac.new(f"ro6votqwe9rtyi@lpnthe9end1ck".encode(), f"{voto.id_voto}|{voto.id_eleicao}|{voto.id_candidato}".encode(), hashlib.sha256).hexdigest()
        if voto.hash_voto != voto_hash:   
            return False
        return True
    
    def get_comprovante_voto_valido(self, comprovante):
        if hasattr(comprovante, 'id_eleitor'):
            return False
        return True
    
    def get_comprovante_voto_unico(self, id_comprovante_voto):
        if repository.get_voto(id_comprovante_voto):
            return False
        return True