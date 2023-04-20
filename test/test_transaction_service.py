from unittest import TestCase
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
        request1 = AccountCreationRequest()
        request1.set_first_name("Spencer")
        request1.set_last_name("James")
        request1.set_pin("1234")
        request1.set_email_address("spencer@gmail.com")
        self.account1 = self.account_service.create_new_account(request1)

        request2 = AccountCreationRequest()
        request2.set_first_name("Allwell")
        request2.set_last_name("Joshua")
        request2.set_pin("1111")
        request2.set_email_address("allwell@gmail.com")

        self.account2 = self.account_service.create_new_account(request2)
        self.transaction.set_amount(1000.0)
        self.transaction.set_sender_pin("1234")
        self.transaction.set_account_id_num(self.account1.get_id_num())
        self.transaction.set_recipient_account_number(self.account2.get_account_number())
        self.transaction_service.transfer(self.transaction)

    def tearDown(self) -> None:
        self.account_service = AccountServiceImpl()
        self.transaction_service = TransactionServiceImpl()
        self.transaction = TransactionRequest()

    def test_transaction_can_be_found_by_id(self):
        self.assertEqual(1000, self.transaction_service.find_by_id(1).get_amount())

    def test_customer_transaction_history_can_be_found_by_id(self):
        self.transaction.set_amount(1000.0)
        self.transaction.set_sender_pin("1111")
        self.transaction.set_account_id_num(self.account2.get_id_num())
        self.transaction.set_recipient_account_number(self.account1.get_account_number())
        self.transaction_service.transfer(self.transaction)

        self.transaction.set_amount(500.0)
        self.transaction.set_sender_pin("1234")
        self.transaction.set_account_id_num(self.account1.get_id_num())
        self.transaction.set_recipient_account_number(self.account2.get_account_number())
        self.transaction_service.transfer(self.transaction)

        self.assertEqual(4, len(self.transaction_service.find_all_by_account_number(100)))
