import unittest
from unittest.mock import patch
import my_app1

class TestCreatePixTransfers(unittest.TestCase):

    @patch('my_app1.create_pix_transfers')
    def test_create_pix_transfers_successful(self, mock_create_pix_transfers):
        """Testa se a função cria transferências corretamente."""
        # Simula um conjunto de transferências bem-sucedidas
        mock_create_pix_transfers.return_value = [{'id': i, 'status': 'success'} for i in range(10)]

        # Chamada da função a ser testada (aqui, você chamaria a função que utiliza create_pix_transfers)
        transfers = my_app1.create_pix_transfers()
        self.assertEqual(len(transfers), 10)  # Verifica se 10 transferências foram criadas

    @patch('my_app1.create_pix_transfers')
    def test_create_pix_transfers_exception(self, mock_create_pix_transfers):
        """Testa o comportamento da função quando ocorre uma exceção."""
        # Simula uma exceção ao tentar criar transferências
        mock_create_pix_transfers.return_value = None

        # Chamada da função a ser testada
        transfers = my_app1.create_pix_transfers()
        self.assertIsNone(transfers)  # Espera-se que a função retorne None em caso de exceção

if __name__ == '__main__':
    unittest.main()
