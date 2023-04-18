from unittest import TestCase

from e_wallet_app.data.models.transaction import Transaction
from e_wallet_app.data.repositories.transaction_repository.transaction_repository_impl import TransactionRepositoryImpl
from e_wallet_app.dtos.reponse.transaction_response import TransactionResponse
from e_wallet_app.dtos.request.transaction_request import TransactionRequest
from e_wallet_app.services.transaction_service import TransactionService
from e_wallet_app.services.transaction_service_impl import TransactionServiceImpl



class TestTransactionService(TestCase):

    transaction_service: TransactionService
    transaction: Transaction

    def setUp(self) -> None:
        self.transaction_service = TransactionServiceImpl()
        self.transaction = Transaction()
        self.transactionR = TransactionRepositoryImpl()
        self

    def test_that_account_a_can_transfer_to_account_b(self):
        self.transaction.set_account_id_num(1)
        self.transaction.set_recipient_account_number(2)
        self.transaction.set_amount(1000)
        self.transaction.set_sender_pin("1234")

    def test_get_list_of_transaction_by_account_id(self):
        self.transaction.set_account_id_num(1)
        self.transaction.set_recipient_account_number(2)
        self.transaction.set_amount(1000)
        self.transaction.set_sender_pin("1234")
        request = TransactionRequest()
        transactions = self.transaction_service.ge
        self.assertEqual(len(transactions), 1)
        for transaction in transactions:
            self.assertIsInstance(transaction, TransactionResponse)
        self.assertEqual(self.transactionR.find_all_by_account_id(1), request.g)

    def test_find_all_transactions(self):
        all_transactions = self.transaction_service.find_all_transactions()
        self.assertGreaterEqual(len(all_transactions), 1)
        for transaction in all_transactions:
            self.assertIsInstance(transaction, TransactionResponse)

