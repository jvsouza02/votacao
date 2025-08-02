from pydantic import BaseModel

class VotoRequestModel(BaseModel):
    id_eleicao: str
    id_eleitor: str
    id_candidato: int

class ComprovanteVotoModel(BaseModel):
    id_comprovante_voto: str
    id_eleicao: int
    data_voto: str
    data_geracao: str

class VotoResponseModel(BaseModel):
    sucesso: bool
    mensagem: str
    comprovante: ComprovanteVotoModel