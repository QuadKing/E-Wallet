from e_wallet_app.dtos.request.account_creation_request import AccountCreationRequest


class AccountService:

    def create_account(self, create: AccountCreationRequest) -> AccountCreationRequest:
        raise NotImplementedError



