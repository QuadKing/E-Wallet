from typing import List, Type

from e_wallet_app.data.repositories.account_repository.account_repository import AccountRepository
from e_wallet_app.dtos.response.account_response import AccountResponse
from e_wallet_app.services.account_service import AccountService
from e_wallet_app.utils.mapper import Mapper


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
