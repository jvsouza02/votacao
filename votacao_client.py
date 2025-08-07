import grpc
from src.protos import votacao_pb2, votacao_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = votacao_pb2_grpc.VotacaoServiceStub(channel)

    # voto_request = votacao_pb2.VotoRequest(
    #     id_eleicao=1,
    #     id_eleitor=26,
    #     id_candidato=7
    # )
    # voto_response = stub.Votar(voto_request)
    # print("Votar:", voto_response.sucesso, voto_response.mensagem)

    voto_valido_request = votacao_pb2.VotoValidoRequest(id_voto="e58b3d4b-0184-4670-a3d0-296164330ca5")
    voto_valido_response = stub.GetVotoValido(voto_valido_request)
    print("Voto válido:", voto_valido_response.valido, voto_valido_response.mensagem)

    # eleicao_votos_request = votacao_pb2.EleicaoVotosRequest(id_eleicao="2")
    # eleicao_votos_response = stub.GetEleicaoVotos(eleicao_votos_request)

    # print("Votos da eleição:")
    # for voto in eleicao_votos_response.votos:
    #     print(f"ID Voto: {voto.id_voto} | Candidato: {voto.id_candidato} | Data: {voto.data_voto}")

if __name__ == '__main__':
    run()
