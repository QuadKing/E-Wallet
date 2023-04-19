from e_wallet_app.data.models.account import Account
from e_wallet_app.dtos.response.account_response import AccountResponse


class AccountService:
    def find_account_by_id(self, id: int) -> AccountResponse:
        raise NotImplementedError

