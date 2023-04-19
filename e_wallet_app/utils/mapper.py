from e_wallet_app.data.models.account import Account
from e_wallet_app.data.models.transaction import Transaction
from e_wallet_app.dtos.request.account_creation_request import AccountCreationRequest
from e_wallet_app.dtos.request.transaction_request import TransactionRequest
from e_wallet_app.dtos.response.account_response import AccountResponse
from e_wallet_app.dtos.response.transaction_response import TransactionResponse


def map(response: AccountResponse, account: Account) -> None:
    response.set_name(account.get_first_name()+" "+account.get_last_name())
    response.set_id_num(account.get_id_num())
    response.set_email_address(account.get_email_address())
    response.set_account_number(account.get_account_number())


def map_account_request_into_account(request: AccountCreationRequest) -> Account:
    account: Account = Account()
    account.set_first_name(request.get_first_name())
    account.set_last_name(request.get_last_name())
    account.set_pin(request.get_pin())
    account.set_email_address(request.get_email_address())
    return account


def map_account_to_response(response: AccountResponse, account: Account) -> None:
    response.set_name(account.get_first_name()+" "+account.get_last_name())
    response.set_id_num(account.get_id_num())
    response.set_email_address(account.get_email_address())
    response.set_account_number(account.get_account_number())


def map_account_into_response(account: Account) -> AccountResponse:
    response: AccountResponse = AccountResponse()
    response.set_name(account.get_first_name() + " " + account.get_last_name())
    response.set_account_number(account.get_account_number())
    response.set_email_address(account.get_email_address())
    response.set_id_num(account.get_id_num())
    return response


def map_transaction_request_to_transaction(request: TransactionRequest) -> Transaction:
    transaction: Transaction = Transaction()
    transaction.set_account_id_num(request.get_account_id_num())
    transaction.set_amount(request.get_amount())
    transaction.set_sender_pin(request.get_sender_pin())
    transaction.set_recipient_account_number(request.get_recipient_account_number())
    return transaction


def map_transaction_to_transaction_response(transaction: Transaction):
    response: TransactionResponse = TransactionResponse()
    response.set_id_num(transaction.get_id_num())
    response.set_amount(transaction.get_amount())
    response.set_recipient_account_number(transaction.get_recipient_account_number())
    response.set_account_id_num(transaction.get_account_id_num())
    return response

def map_transaction_history_to_transaction_responses(transactions):
    transaction_responses: list[TransactionResponse] = []
    for each in transactions:
        transaction_responses.append(map_transaction_to_transaction_response(each))
    return transaction_responses
