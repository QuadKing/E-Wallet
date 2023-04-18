from e_wallet_app.data.models.account import Account
from e_wallet_app.dtos.response.account_response import AccountResponse


class Mapper:
    def map(self, found_account: Account, account_response: AccountResponse) -> None:
        account_response.set_first_name(found_account.get_first_name())
        account_response.set_last_name(found_account.get_last_name())
        account_response.set_account_number(found_account.get_account_number())
        account_response.set_email_address(found_account.get_email_address())
