from e_wallet_app.dtos.request.account_creation_request import AccountCreationRequest
from e_wallet_app.dtos.response.account_response import AccountResponse
from e_wallet_app.exceptions.invalid_credential_exception import InvalidCredentialException
from e_wallet_app.services.account_service import AccountService
from e_wallet_app.services.account_service_impl import AccountServiceImpl


class AccountController:

    def __init__(self):
        self.__account_service: AccountService = AccountServiceImpl()

    def create_new_account(self, account_creation_request: AccountCreationRequest) -> AccountResponse:
        return self.__account_service.create_new_account(account_creation_request)
