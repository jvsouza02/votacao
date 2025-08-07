from fastapi import FastAPI
import grpc
from src.protos import votacao_pb2, votacao_pb2_grpc
from src.models.voto_request_response import VotoResponseModel, VotoRequestModel, ComprovanteVotoModel, VotosRequestModel, VotosResponseModel

app = FastAPI()

@app.post('/votar', response_model=VotoResponseModel)
async def votar(request: VotoRequestModel):
    channel = grpc.insecure_channel('grpc_server:50051')
    stub = votacao_pb2_grpc.VotacaoServiceStub(channel)

    voto_request = votacao_pb2.VotoRequest(
        id_eleicao=request.id_eleicao,
        id_eleitor=int(request.id_eleitor),
        id_candidato=request.id_candidato
    )

    voto_response = stub.Votar(voto_request)

    return {
        'sucesso': voto_response.sucesso,
        'mensagem': voto_response.mensagem,
        'comprovante': ComprovanteVotoModel(
            id_comprovante_voto=voto_response.comprovante.id_comprovante_voto,
            id_eleicao=voto_response.comprovante.id_eleicao,
            data_voto=voto_response.comprovante.data_voto,
            data_geracao=voto_response.comprovante.data_geracao
        )
    }

@app.get('/votos', response_model=list[VotosResponseModel])
async def votos(request: VotosRequestModel = VotosRequestModel(id_eleicao="")):
    channel = grpc.insecure_channel('grpc_server:50051')
    stub = votacao_pb2_grpc.VotacaoServiceStub(channel)

    voto_request = votacao_pb2.EleicaoVotosRequest(
        id_eleicao=request.id_eleicao
    )

    voto_response = stub.GetEleicaoVotos(voto_request)

    return [
        VotosResponseModel(
            id_voto=voto.id_voto,
            id_candidato=voto.id_candidato,
            data_voto=voto.data_voto
        ) for voto in voto_response.votos
    ]