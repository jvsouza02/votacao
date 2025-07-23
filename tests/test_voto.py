import unittest
from unittest.mock import MagicMock, patch
from domains.voto import Voto
from repositories.voto_repository import VotoRepository
from services.votacao_service import VotacaoService

class TestVoto(unittest.TestCase):
    voto_path = 'domains.voto.VotacaoService'

    def setUp(self):
        self.repositorio_mock = MagicMock(spec=VotoRepository)
        self.voto = Voto(id_eleicao=1, id_eleitor=1, id_candidato=1)
        self.hash_voto = self.voto.gerar_hash()
        self.votacao_service = VotacaoService()

    @patch(f"{voto_path}.get_voto_existente")
    def test_voto_unico(self, mock_get_voto_existente):
        mock_get_voto_existente.return_value = None
        resultado = self.voto.validar_voto_unico()
        self.assertTrue(resultado)

    @patch(f'{voto_path}.get_eleicao_ativa')
    def test_eleicao_ativa(self, mock_get_eleicao_ativa):
        mock_get_eleicao_ativa.return_value = {"id_eleicao": 1, "status": "ativa"}
        resultado = self.voto.validar_eleicao_ativa()
        self.assertTrue(resultado)

    @patch(f'{voto_path}.get_candidato_valido')
    def test_candidato_valido(self, mock_get_candidato_valido):
        mock_get_candidato_valido.return_value = {"id_eleicao": 1, "nome": "Candidato Teste"}
        resultado = self.voto.validar_candidato()
        self.assertTrue(resultado)

    @patch(f'{voto_path}.get_voto_valido')
    def test_integridade_voto(self, mock_get_voto_valido):
        mock_get_voto_valido.return_value = {"id_eleicao": 1, "id_eleitor": 1, "id_candidato": 1, 'hash_voto': self.hash_voto, 'data_voto': self.voto.data_voto}
        resultado = self.voto.validar_integridade_voto()
        self.assertTrue(resultado)
   
if __name__ == '__main__':
    unittest.main()