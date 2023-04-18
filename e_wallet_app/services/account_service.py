from e_wallet_app.dtos.request.account_creation_request import AccountCreationRequest

from e_wallet_app.dtos.response.account_response import AccountResponse


class AccountService:

    def find_all_account(self) -> list[AccountResponse]:
        raise NotImplementedError

    def create_new_account(self, request: AccountCreationRequest) -> AccountResponse:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError
