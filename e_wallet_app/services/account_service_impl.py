
from typing import List, Type
from e_wallet_app.data.repositories.account_repository.account_repository import AccountRepository
from e_wallet_app.utils.mapper import Mapper
from e_wallet_app.data.models.account import Account
from e_wallet_app.data.repositories.account_repository.account_repository_impl import AccountRepositoryImpl
from e_wallet_app.dtos.request.account_creation_request import AccountCreationRequest
from e_wallet_app.dtos.response.account_response import AccountResponse
from e_wallet_app.exceptions.duplicate_account_exception import DuplicateAccountException
from e_wallet_app.services.account_service import AccountService
from e_wallet_app.services.transaction_service import TransactionService
from e_wallet_app.services.transaction_service_impl import TransactionServiceImpl
from e_wallet_app.utils import mapper


class AccountServiceImpl(AccountService):

    __account_repository: AccountRepository = AccountRepository()
    def find_all_account(self) -> list[Type[AccountResponse] | None]:
        account_response: AccountResponse = AccountResponse()
        accounts = self.__account_repository.find_all_account()
        account_response_list = [AccountResponse]
        for account in accounts:
            Mapper.map(account, account_response)
            account_response_list.append(account_response)

        return account_response_list

    def __init__(self):
        self.__account_repository: AccountRepositoryImpl = AccountRepositoryImpl()
        self.__transaction_service: TransactionService = TransactionServiceImpl()
        self.__account_number_generator: int = 99

    def create_new_account(self, request: AccountCreationRequest) -> AccountResponse:
        self.validate_duplicate_account(request.get_email_address())
        account: Account = mapper.map_account_request_into_account(request)
        account.set_account_number(self.generate_account_number())
        found_account: Account = self.__account_repository.save(account)
        response: AccountResponse = mapper.map_account_into_response(found_account)
        response.set_balance(self.generate_balance(response.get_account_number()))
        return response

    def count(self) -> int:
        return self.__account_repository.count()

    def generate_account_number(self):
        self.__account_number_generator += 1
        return self.__account_number_generator

    def generate_balance(self, account_number: int) -> float:
        return self.__transaction_service.get_balance_by_account_number(account_number)

    def validate_duplicate_account(self, email_address: str):
        if self.__account_repository.find_by_email_address(email_address) is not None:
            raise DuplicateAccountException()

