from e_wallet_app.data.models.account import Account
from e_wallet_app.data.repositories.account_repository.account_repository import AccountRepository
from e_wallet_app.data.repositories.account_repository.account_repository_impl import AccountRepositoryImpl
from e_wallet_app.dtos.response.account_response import AccountResponse
from e_wallet_app.services.account_service import AccountService
from e_wallet_app.utils.mapper import Mapper


class AccountServiceImpl(AccountService):
    account_Repository: AccountRepository = AccountRepositoryImpl()

    def find_account_by_id(self, id: int) -> AccountResponse:
        self.validate_account_id(id)
        account: Account = self.account_Repository.find_by_id(self.id)
        response: AccountResponse = AccountResponse()
        Mapper.map(response, account)
        return response

    def validate_account_id(self, id: int) -> None:
        if self.account_Repository.find_by_id(id) is None:
            raise ValueError("Account does not exist")
