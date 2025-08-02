from fastapi import FastAPI
from pydantic import BaseModel
import grpc
from src.protos import votacao_pb2, votacao_pb2_grpc
from src.models.voto_request_response import VotoResponseModel, VotoRequestModel, ComprovanteVotoModel

app = FastAPI()

@app.post('/votar', response_model=VotoResponseModel)
async def votar(request: VotoRequestModel):
    channel = grpc.insecure_channel('localhost:50051')
    stub = votacao_pb2_grpc.VotacaoServiceStub(channel)

    voto_request = votacao_pb2.VotoRequest(
        id_eleicao=request.id_eleicao,
        id_eleitor=request.id_eleitor,
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