from e_wallet_app.data.models.account import Account
from e_wallet_app.data.repositories.account_repository.account_repository import AccountRepository
from e_wallet_app.data.repositories.account_repository.account_repository_impl import AccountRepositoryImpl
from e_wallet_app.dtos.response.account_response import AccountResponse
from e_wallet_app.services.account_service import AccountService
from e_wallet_app.utils.mapper import Mapper


class AccountServiceImpl(AccountService):
    account_Repository: AccountRepository = AccountRepositoryImpl()

