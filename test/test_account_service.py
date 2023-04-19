from unittest import TestCase
from e_wallet_app.data.models.account import Account
from e_wallet_app.data.repositories.account_repository.account_repository_impl import AccountRepositoryImpl
from e_wallet_app.dtos.request.account_creation_request import AccountCreationRequest
from e_wallet_app.dtos.response.account_response import AccountResponse
from e_wallet_app.exceptions.duplicate_account_exception import DuplicateAccountException
from e_wallet_app.services.account_service import AccountService
from e_wallet_app.services.account_service_impl import AccountServiceImpl


class TestAccountService(TestCase):
    account_service: AccountService
    account: Account
    account_request: AccountCreationRequest
    account_response: AccountResponse

    def setUp(self) -> None:
        self.account_service = AccountServiceImpl()
        self.account = Account()
        self.account_repository = AccountRepositoryImpl()
        self.account_response = AccountResponse()
        self.account_service = AccountServiceImpl()
        self.account_request = AccountCreationRequest()
        self.account_request.set_first_name("Prof")
        self.account_request.set_last_name("Marvellous")
        self.account_request.set_email_address("profmarv@gmail.com")
        self.account_request.set_pin("1234")
        self.account_response = self.account_service.create_new_account(self.account_request)

    def test_account_can_be_find_by_id(self):
        self.account = Account()
        self.account_request = AccountCreationRequest()
        self.account_service.create_new_account(self.account_request)
        self.assertEquals("Prof", self.account_service.find_account_by_id(1).get_first_name())

    def test_account_can_be_created(self):
        self.assertEqual(1, self.account_service.count())
        self.assertEqual(1, self.account_response.get_id_num())

    def test_account_number_can_be_generated_at_creation(self):
        self.assertEqual(100, self.account_response.get_account_number())

    def test_account_with_same_email_address_cannot_be_created(self):
        with self.assertRaises(DuplicateAccountException):
            self.account_service.create_new_account(self.account_request)

    def test_account_is_credited_a_joining_bonus_of_1000_at_registration(self):
        self.assertEqual(1000, self.account_response.get_balance())

