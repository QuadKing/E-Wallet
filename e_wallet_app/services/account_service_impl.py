from e_wallet_app.data.models.account import Account
from e_wallet_app.data.repositories.account_repository.account_repository_impl import AccountRepositoryImpl
from e_wallet_app.dtos.request.account_creation_request import AccountCreationRequest
from e_wallet_app.dtos.request.transaction_request import TransactionRequest
from e_wallet_app.dtos.response.account_response import AccountResponse
from e_wallet_app.exceptions.account_does_not_exist_exception import AccountDoesNotExistException
from e_wallet_app.exceptions.duplicate_account_exception import DuplicateAccountException
from e_wallet_app.services.account_service import AccountService
from e_wallet_app.services.transaction_service import TransactionService
from e_wallet_app.services.transaction_service_impl import TransactionServiceImpl
from e_wallet_app.utils import mapper


class AccountServiceImpl(AccountService):
    def __init__(self):
        self.WALLET_ID = 0
        self.JOINING_BONUS: float = 1000.0
        self.__account_repository: AccountRepositoryImpl = AccountRepositoryImpl()
        self.__transaction_service: TransactionService = TransactionServiceImpl()
        self.__account_number_generator: int = 99

    def find_account_by_id(self, id: int) -> AccountResponse:
        self.validate_account_id(id)
        account: Account = self.__account_repository.find_by_id(id)
        response: AccountResponse = AccountResponse()
        mapper.map(response, account)
        self.set_balance(response)
        return response

    def validate_account_id(self, id: int) -> None:
        if self.__account_repository.find_by_id(id) is None:
            raise AccountDoesNotExistException()

    def create_new_account(self, request: AccountCreationRequest) -> AccountResponse:
        self.validate_duplicate_account(request.get_email_address())
        account: Account = mapper.map_account_request_into_account(request)
        account.set_account_number(self.generate_account_number())
        found_account: Account = self.__account_repository.save(account)
        response: AccountResponse = mapper.map_account_into_response(found_account)
        self.add_joining_bonus(response)
        response.set_balance(self.generate_balance(response))
        return response

    def count(self) -> int:
        return self.__account_repository.count()

    def generate_account_number(self):
        self.__account_number_generator += 1
        return self.__account_number_generator

    def generate_balance(self, response: AccountResponse) -> float:
        return self.__transaction_service.get_balance_by_account_number(response)

    def validate_duplicate_account(self, email_address: str):
        if self.__account_repository.find_by_email_address(email_address) is not None:
            raise DuplicateAccountException()

    def find_by_account_number(self, account_number: int) -> AccountResponse:
        account: Account = self.__account_repository.find_by_account_number(account_number)
        if account is None:
            raise AccountDoesNotExistException()
        response: AccountResponse = AccountResponse()
        mapper.map(response, account)
        self.set_balance(response)
        return response

    def set_balance(self, response):
        response.set_balance(self.__transaction_service.get_balance_by_account_number(response))

    def add_joining_bonus(self, response: AccountResponse):
        transaction_request: TransactionRequest = TransactionRequest()
        transaction_request.set_amount(self.JOINING_BONUS)
        transaction_request.set_recipient_account_number(response.get_account_number())
        transaction_request.set_account_id_num(self.WALLET_ID)
        self.__transaction_service.transfer(transaction_request)

