from fastapi import FastAPI
import grpc
from src.protos import votacao_pb2, votacao_pb2_grpc

app = FastAPI()

@app.post('/votar')
async def votar(request: votacao_pb2.VotoRequest):
    channel = grpc.insecure_channel('localhost:50051')
    stub = votacao_pb2_grpc.VotacaoServiceStub(channel)
    voto_request = votacao_pb2.VotoRequest(
        id_eleicao=request.id_eleicao,
        id_eleitor=request.id_eleitor,
        id_candidato=request.id_candidato
    )
    voto_response = stub.Votar(voto_request)
    return voto_response