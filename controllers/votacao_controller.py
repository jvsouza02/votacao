import grpc
import datetime
from tasks import voto_task
from protos import votacao_pb2, votacao_pb2_grpc
from services.votacao_service import VotacaoService

class VotacaoController(votacao_pb2_grpc.VotacaoServiceServicer):
    def __init__(self):
        self.votacao_service = VotacaoService()

    def Votar(self, request, context):
        try:
            voto_result = voto_task.processar_voto.delay(
                id_eleicao=request.id_eleicao,
                id_eleitor=request.id_eleitor,
                id_candidato=request.id_candidato
            )

            comprovante_voto = voto_result.get(timeout=30)
            data_voto = datetime.fromisoformat(comprovante_voto['data_voto'])
            data_geracao = datetime.fromisoformat(comprovante_voto['data_geracao'])

            return votacao_pb2.VotoResponse(
                sucesso=True,
                mensagem="Voto computado com sucesso.",
                comprovante=votacao_pb2.ComprovanteVoto(
                    id_comprovante_voto=str(comprovante_voto['id_comprovante_voto']),
                    id_eleicao=int(comprovante_voto['id_eleicao']),
                    data_voto=data_voto.strftime('%Y-%m-%d %H:%M:%S'),
                    data_geracao=data_geracao.strftime('%Y-%m-%d %H:%M:%S')
                )
            )
        
        except ValueError as err:
            return votacao_pb2.VotoResponse(
                sucesso=False,
                mensagem=repr(err)
            )

    def GetVotoValido(self, request, context):
        try:
            valido, mensagem = self.votacao_service.get_voto_valido(request.id_voto)
            return votacao_pb2.VotoValidoResponse(
                valido=valido,
                mensagem=mensagem
            )
        except Exception as err:
            return votacao_pb2.VotoValidoResponse(
                valido=False,
                mensagem=str(err)
            )

    def GetEleicaoVotos(self, request, context):
        try:
            votos = self.votacao_service.get_eleicao_votos(request.id_eleicao)
            votos_info = []
            for voto in votos:
                votos_info.append(
                    votacao_pb2.VotoInfo(
                        id_voto=str(voto.id_voto),
                        id_candidato=voto.id_candidato,
                        data_voto=voto.data_voto.strftime('%Y-%m-%d %H:%M:%S')
                    )
                )
            return votacao_pb2.EleicaoVotosResponse(votos=votos_info)
        except Exception as err:
            context.set_details(str(err))
            context.set_code(grpc.StatusCode.INTERNAL)
            return votacao_pb2.EleicaoVotosResponse()
