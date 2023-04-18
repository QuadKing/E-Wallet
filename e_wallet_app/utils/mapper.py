from e_wallet_app.data.models.account import Account

from e_wallet_app.dtos.request.account_creation_request import AccountCreationRequest
from e_wallet_app.dtos.response.account_response import AccountResponse


def map(response: AccountResponse, account: Account) -> None:
    response.set_first_name(account.get_first_name())
    response.set_id_num(account.get_id_num())
    response.set_email_address(account.get_email_address())
    response.set_account_number(account.get_account_number())
    response.set_last_name(account.get_last_name())


def map_account_request_into_account(request: AccountCreationRequest) -> Account:
    account: Account = Account()
    account.set_first_name(request.get_first_name())
    account.set_last_name(request.get_last_name())
    account.set_pin(request.get_pin())
    account.set_email_address(request.get_email_address())
    return account


def map_account_into_response(account: Account) -> AccountResponse:
    response: AccountResponse = AccountResponse()
    response.set_name(account.get_first_name() + " " + account.get_last_name())
    response.set_account_number(account.get_account_number())
    response.set_email_address(account.get_email_address())
    response.set_id_num(account.get_id_num())
    return response
