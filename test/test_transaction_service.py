from unittest import TestCase

from e_wallet_app.data.repositories.transaction_repository.transaction_repository_impl import TransactionRepositoryImpl
from e_wallet_app.dtos.request.account_creation_request import AccountCreationRequest
from e_wallet_app.dtos.request.transaction_request import TransactionRequest
from e_wallet_app.dtos.response.account_response import AccountResponse
from e_wallet_app.services.account_service import AccountService
from e_wallet_app.services.account_service_impl import AccountServiceImpl
from e_wallet_app.services.transaction_service import TransactionService
from e_wallet_app.services.transaction_service_impl import TransactionServiceImpl


class TestTransactionService(TestCase):
    transaction_service: TransactionService
    transaction: TransactionRequest
    account_service: AccountService
    account1: AccountResponse
    account2: AccountResponse

    def setUp(self) -> None:
        self.account_service = AccountServiceImpl()
        self.transaction_service = TransactionServiceImpl()
        self.transaction = TransactionRequest()
        self.transaction_repository = TransactionRepositoryImpl()
        request1 = AccountCreationRequest()
        request1.first_name = "Spencer"
        request1.last_name = "James"
        request1.pin = "1234"
        request1.email_address = "spencer@gmail.com"
        self.account1 = self.account_service.create_new_account(request1)
        request2 = AccountCreationRequest()
        request2.set_first_name("Allwell")
        request2.set_last_name("Joshua")
        request2.set_pin("1111")
        request2.set_email_address("allwell@gmail.com")
        self.account2 = self.account_service.create_new_account(request2)
        self.transaction.amount = 1000.0
        self.transaction.sender_pin = "1234"

    def tearDown(self) -> None:
        self.account_service = None
        self.transaction_service = None
        self.transaction = None

    def test_find_all_transactions(self):
        self.transaction.set_amount(500)
        self.transaction.set_sender_pin("1111")
        self.transaction.set_account_id_num(self.account2.id_num)
        self.transaction.set_recipient_account_number(self.account1.account_number)
        self.transaction_service.transfer(self.transaction)

        self.assertEqual(500, self.transaction_service.find_by_id(1).amount)
        self.assertEqual(500.0, self.transaction_service.find_all_transactions())

    def test_find_all_by_account_number(self):
        self.transaction.amount = 1000.0
        self.transaction.sender_pin = "1111"
        self.transaction.account_id_num = self.account2.id_num
        self.transaction.recipient_account_number = self.account1.account_number
        self.transaction_service.transfer(self.transaction)
        self.assertEqual(1000, self.transaction_service.find_by_id(1).amount)
        self.assertEqual(2, len(self.transaction_service.find_all_by_account_number(100)))
        self.transaction.amount = 1500.0
        self.transaction.sender_pin = "1111"
        self.transaction.account_id_num = self.account1.id_num
        self.transaction.recipient_account_number = self.account2.account_number
        self.transaction_service.transfer(self.transaction)
        self.transaction.amount = 500.0
        self.transaction.sender_pin = "1111"
        self.transaction.account_id_num = self.account2.id_num
        self.transaction.recipient_account_number = self.account1.account_number
        self.transaction_service.transfer(self.transaction)
        self.transaction.amount = 1000.0
        self.transaction.sender_pin = "1111"
        self.transaction.account_id_num = self.account1.id_num
        self.transaction.recipient_account_number = self.account2.account_number
        self.transaction_service.transfer(self.transaction)

        self.transaction.set_amount(500.0)
        self.transaction.set_sender_pin("1234")
        self.transaction.set_account_id_num(self.account1.get_id_num())
        self.transaction.set_recipient_account_number(self.account2.get_account_number())
        self.transaction_service.transfer(self.transaction)

        self.assertEqual(4, len(self.transaction_service.find_all_by_account_number(100)))
