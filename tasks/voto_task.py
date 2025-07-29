from worker import app
from services.votacao_service import VotacaoService
from domains.voto import Voto

@app.task(bind=True)
def processar_voto(self, id_eleicao, id_eleitor, id_candidato):
    service = VotacaoService()
    voto = Voto(id_eleicao=id_eleicao, id_eleitor=id_eleitor, id_candidato=id_candidato)
    try:
        return service.votar(voto)
    except Exception as e:
        raise self.retry(exc=e, countdown=30)