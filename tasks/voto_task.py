from worker import app
from services.votacao_service import VotacaoService

@app.task(bind=True)
def processar_voto(self, id_eleicao, id_eleitor, id_candidato):
    service = VotacaoService()
    try:
        return service.votar(id_eleicao, id_eleitor, id_candidato)
    except Exception as e:
        raise self.retry(exc=e, countdown=30)