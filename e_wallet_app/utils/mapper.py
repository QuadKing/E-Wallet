from e_wallet_app.data.models.account import Account
from e_wallet_app.dtos.response.account_response import AccountResponse


class Mapper:


    def map(self, response: AccountResponse, account: Account)-> None:
        response.set_first_name(account.get_first_name())
        response.set_id_num(account.get_id_num())
        response.set_email_address(account.get_email_address())
        response.set_account_number(account.get_account_number())
        response.set_last_name(account.get_last_name())