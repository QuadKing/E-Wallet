from e_wallet_app.dtos.request.account_creation_request import AccountCreationRequest
from e_wallet_app.dtos.response.account_response import AccountResponse


class AccountService:

    def find_account_by_id(self, id: int) -> AccountResponse:
        raise NotImplementedError

    def create_new_account(self, request: AccountCreationRequest) -> AccountResponse:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError

    def find_by_account_number(self, account_number: int) -> AccountResponse:
        raise NotImplementedError


