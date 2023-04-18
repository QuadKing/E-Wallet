from e_wallet_app.dtos.response.account_response import AccountResponse


class AccountService:

    def find_all_account(self) -> list[AccountResponse]:
        raise NotImplementedError
