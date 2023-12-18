import unittest
from my_app1 import api, create_transfer, get_transfer_status
from unittest.mock import patch

class CreateTransferTest(unittest.TestCase):

    def test_create_transfer_with_invalid_account_type(self):
        """Testa se ValueError é lançado para tipo de conta inválido."""
        client = api.Client()

        with self.assertRaises(ValueError) as context:
            transfer = client.pix.transfers.create(
                amount=100,
                sender_id="1",
                receiver_id="2",
                account_type="INVALID",
            )
        self.assertEqual(str(context.exception), "Expected error message")

class GetTransferStatusTest(unittest.TestCase):

    @patch('my_app1.api.Client.pix.transfers.get_status')
    def test_get_transfer_status_processing(self, mock_get_status):
        """Testa se o status 'processing' é retornado corretamente."""
        mock_get_status.return_value = {'status': "processing"}

        client = api.Client()
        transfer_id = "1234567890"
        transfer_status = client.pix.transfers.get_status(transfer_id)

        self.assertEqual(transfer_status['status'], "processing")

if __name__ == "__main__":
    unittest.main()
