from unittest import TestCase

from e_wallet_app.data.models.account import Account
from e_wallet_app.data.repositories.account_repository.account_repository import AccountRepository
from e_wallet_app.data.repositories.account_repository.account_repository_impl import AccountRepositoryImpl


class TestAccountRepository(TestCase):
    account_repository: AccountRepository
    account1: Account

    def setUp(self) -> None:
        self.account_repository = AccountRepositoryImpl()
        self.account1 = Account()
        self.account_repository.save(self.account1)

    def test_account_can_be_saved(self):
        self.assertEqual(1, self.account_repository.count())

    def test_id_is_automatically_generated_upon_saving(self):
        self.assertEqual(1, self.account1.get_id_num())

    def test_save_one_account_twice_count_is_one(self):
        self.account_repository.save(self.account1)
        self.assertEqual(1, self.account_repository.count())

    def test_account_can_be_found_by_id(self):
        account2: Account = Account()
        account2.set_first_name("Moyin")
        self.account_repository.save(account2)
        self.assertEqual(2, self.account_repository.count())
        self.assertEqual("Moyin", self.account_repository.find_by_id(2).get_first_name())

    def test_account_can_be_found_by_account_number(self):
        account2: Account = Account()
        self.account_repository.save(account2)
        self.assertEqual(2, self.account_repository.count())
        self.assertEqual(1, self.account_repository.find_by_account_number(0).get_id_num())






