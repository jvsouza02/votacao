import unittest
from unittest.mock import MagicMock, patch
from domains.comprovante_voto import ComprovanteVoto
from domains.voto import Voto
from repositories.voto_repository import VotoRepository
from services.votacao_service import VotacaoService

class TestGerarComprovante(unittest.TestCase):
    comprovante_voto_path = 'domains.comprovante_voto.ComprovanteVotacaoService'

    def setUp(self):
        self.repository_mock = MagicMock(spec=VotoRepository)
        self.voto = Voto(id_eleicao=1, id_eleitor=101, id_candidato=1)
        self.voto.gerar_hash()
        self.comprovante = ComprovanteVoto(self.voto)
        self.votacao_service = VotacaoService()

    @patch(f'{comprovante_voto_path}.get_voto_valido')
    def test_gera_comprovante_para_voto_valido(self, mock_get_voto_valido):
        mock_get_voto_valido.return_value = True
        resultado = self.comprovante.validar_comprovante_para_voto_valido()
        self.assertTrue(resultado)

    @patch(f'{comprovante_voto_path}.get_comprovante_voto_valido')
    def test_comprovante_nao_expoe_voto(self, mock_get_comprovante_voto_valido):
        mock_get_comprovante_voto_valido.return_value = True
        resultado = self.comprovante.validar_comprovante_nao_expoe_voto(self.comprovante)
        self.assertTrue(resultado)

    @patch(f'{comprovante_voto_path}.get_comprovante_voto_unico')
    def test_comprovante_gerado_unico(self, mock_get_comprovante_voto_unico):
        mock_get_comprovante_voto_unico.return_value = True
        resultado = self.comprovante.validar_comprovante_voto_unico(self.comprovante.id_comprovante_voto)
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()