from pydantic import BaseModel

class VotoRequestModel(BaseModel):
    id_eleicao: str
    id_eleitor: int
    id_candidato: str

class ComprovanteVotoModel(BaseModel):
    id_comprovante_voto: str
    id_eleicao: str
    data_voto: str
    data_geracao: str

class VotoResponseModel(BaseModel):
    sucesso: bool
    mensagem: str
    comprovante: ComprovanteVotoModel

class VotosRequestModel(BaseModel):
    id_eleicao: str

class VotosResponseModel(BaseModel):
    id_voto: str
    id_candidato: str
    data_voto: str

