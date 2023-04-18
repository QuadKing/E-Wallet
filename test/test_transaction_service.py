from unittest import TestCase

from e_wallet_app.data.models.transaction import Transaction
from e_wallet_app.services.transaction_service import TransactionService
from e_wallet_app.services.transaction_service_impl import TransactionServiceImpl


class TestTransactionService(TestCase):

    transaction_service: TransactionService
    transaction: Transaction

    def setUp(self) -> None:
        self.transaction_service = TransactionServiceImpl()
        self.transaction = Transaction()

    def test_that_account_a_can_transfer_to_account_b(self):
        self.transaction.set_account_id_num(1)
        self.transaction.set_recipient_account_number(2)
        self.transaction.set_amount(1000)
        self.transaction.set_sender_pin("1234")