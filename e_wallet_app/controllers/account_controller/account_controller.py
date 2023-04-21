from typing import List

from e_wallet_app.data.models.account import Account
from e_wallet_app.data.repositories.account_repository.account_repository import AccountRepository
from e_wallet_app.data.repositories.account_repository.account_repository_impl import AccountRepositoryImpl
from e_wallet_app.dtos.request.account_creation_request import AccountCreationRequest
from e_wallet_app.dtos.request.transaction_request import TransactionRequest
from e_wallet_app.dtos.response.account_response import AccountResponse
from e_wallet_app.exceptions.account_does_not_exist_exception import AccountDoesNotExistException
from e_wallet_app.exceptions.duplicate_account_exception import DuplicateAccountException
from e_wallet_app.services.account_service import AccountService
from e_wallet_app.services.account_service_impl import AccountServiceImpl
from e_wallet_app.services.transaction_service import TransactionService
from e_wallet_app.services.transaction_service_impl import TransactionServiceImpl
from e_wallet_app.utils import mapper


class AccountController:
    def __init__(self):
        self.__account_service: AccountService = AccountServiceImpl()

    def get_all_accounts(self) -> List[dict]:
        accounts = self.__account_service.find_all_account()
        return [account.to_dict() for account in accounts]

    def get_account_by_id(self, id_num: int) -> dict:
        try:
            account = self.__account_service.find_account_by_id(id_num)
            return account.to_dict()
        except AccountDoesNotExistException:
            return {"error": "Account does not exist"}

    def create_new_account(self, request_data: dict) -> dict:
        request = AccountCreationRequest.from_dict(request_data)
        try:
            account = self.__account_service.create_new_account(request)
            return account.to_dict()
        except DuplicateAccountException:
            return {"error": "Account with that email already exists"}

    def get_account_balance(self, account_number: int) -> dict:
        try:
            account = self.__account_service.find_by_account_number(account_number)
            return {"balance": account.get_balance()}
        except AccountDoesNotExistException:
            return {"error": "Account does not exist"}

    def transfer_money(self, request_data: dict) -> dict:
        request = TransactionRequest.from_dict(request_data)
        try:
            self.__account_service.transfer(request)
            return {"message": "Transfer successful"}
        except AccountDoesNotExistException:
            return {"error": "Account does not exist"}
        except ValueError as e:
            return {"error": str(e)}
