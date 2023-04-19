from unittest import TestCase

from e_wallet_app.data.models.account import Account
from e_wallet_app.data.repositories.account_repository.account_repository import AccountRepository
from e_wallet_app.data.repositories.account_repository.account_repository_impl import AccountRepositoryImpl
from e_wallet_app.dtos.request.account_creation_request import AccountCreationRequest
from e_wallet_app.services.account_service import AccountService
from e_wallet_app.services.account_service_impli import AccountServiceImpl


class TestAccountService(TestCase):
    account_service: AccountService
    account_repository: AccountRepository
    account : Account
    request: AccountCreationRequest

    def setUp(self) -> None:
       self.account_service = AccountServiceImpl()
       self.account = Account()
       self.account_repository = AccountRepositoryImpl()


    def test_account_can_be_find_by_id(self):
        self.account = Account()
        self.request = AccountCreationRequest()
        self.request.set_account_number(100)
        self.request.set_last_name("Prof")
        self.request.set_first_name("Moyin")
        self.request.set_email_address("ProfMoyin@gmail.com")
        self.request.set_pin("1234")
        self.request.set_password("password")
        self.account_service.find_account_by_id(self, id)





