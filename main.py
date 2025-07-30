import grpc
from concurrent import futures
from src.controllers.votacao_controller import VotacaoController
from src.protos import votacao_pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    votacao_pb2_grpc.add_VotacaoServiceServicer_to_server(VotacaoController(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC iniciado na porta 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()