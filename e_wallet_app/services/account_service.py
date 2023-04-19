
from e_wallet_app.dtos.response.account_response import AccountResponse


class AccountService:

    def create_new_account(self, account_request):
        raise NotImplementedError

    def find_all_account(self) -> list[AccountResponse]:
        raise NotImplementedError

    def find_account_by_id(self, id_num: int) -> AccountResponse:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError
