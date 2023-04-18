from e_wallet_app.data.models import account
from e_wallet_app.dtos.request.account_creation_request import AccountCreationRequest
from e_wallet_app.services.account_service.account_service import AccountService


class AccountServiceImpl(AccountService):
    def create_account(self, create: AccountCreationRequest) -> AccountCreationRequest:
        account_has_not_been_created: bool = account.get_id_num() == 0