
import unittest
from datetime import datetime, timedelta
from ferias_core import dias_para_ferias, excluir_funcionario_por_id
from email_utils import enviar_email_aviso


class TestFeriasExtremos(unittest.TestCase):
    def test_data_ferias_invalida(self):
        # Data inválida deve retornar None
        self.assertIsNone(dias_para_ferias("2025-99-99"))

    def test_excluir_funcionario_id_inexistente(self):
        funcionarios = [
            {"id": 1, "nome": "Ana"},
            {"id": 2, "nome": "Carlos"}
        ]
        novos, removidos = excluir_funcionario_por_id(funcionarios, 99)
        self.assertEqual(len(removidos), 0)
        self.assertEqual(len(novos), 2)

    def test_dias_para_ferias_passadas(self):
        # Data de férias já passada
        data_passada = (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%d")
        dias = dias_para_ferias(data_passada)
        self.assertTrue(dias < 0)


if __name__ == "__main__":
    unittest.main()
