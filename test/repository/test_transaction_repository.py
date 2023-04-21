from unittest import TestCase

from e_wallet_app.data.models.transaction import Transaction
from e_wallet_app.data.repositories.transaction_repository.transaction_repository import TransactionRepository
from e_wallet_app.data.repositories.transaction_repository.transaction_repository_impl import TransactionRepositoryImpl


class TestTransactionRepository(TestCase):
    transaction: Transaction
    transaction_repository: TransactionRepository

    def setUp(self) -> None:
        self.transaction = Transaction()
        self.transaction_repository = TransactionRepositoryImpl()
        self.transaction.set_account_id_num(1)
        self.transaction = self.transaction_repository.save(self.transaction)

    def test_transaction_can_be_saved(self):
        self.assertEqual(1, self.transaction_repository.count())

    def test_id_is_automatically_generated_upon_saving(self):
        self.assertEqual(1, self.transaction.get_id_num())

    def test_save_one_transaction_twice_count_is_one(self):
        self.transaction_repository.save(self.transaction)
        self.assertEqual(1, self.transaction_repository.count())

    def test_transaction_can_be_found_by_id(self):
        transaction2: Transaction = Transaction()
        transaction2.set_amount(1000.0)
        self.transaction_repository.save(transaction2)
        self.assertEqual(2, self.transaction_repository.count())
        self.assertEqual(1000.0, self.transaction_repository.find_by_id(2).get_amount())

    def test_transactions_can_be_found_by_account_id(self):
        transaction2: Transaction = Transaction()
        transaction2.set_account_id_num(1)
        transaction2.set_amount(1000.0)
        self.transaction_repository.save(transaction2)
        self.assertEqual(2, self.transaction_repository.count())
        self.assertEqual(2, len(self.transaction_repository.find_all_by_account_id(1)))






