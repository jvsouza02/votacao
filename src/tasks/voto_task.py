from config.celery import app
from src.services.votacao_service import VotacaoService
from src.domains.voto import Voto

@app.task(bind=True)
def processar_voto(self, id_eleicao, id_eleitor, id_candidato):
    service = VotacaoService()
    voto = Voto(id_eleicao=id_eleicao, id_eleitor=id_eleitor, id_candidato=id_candidato)
    try:
        return service.votar(voto)
    except Exception as e:
        raise e