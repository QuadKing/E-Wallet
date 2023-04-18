from e_wallet_app.data.models.transaction import Transaction
from e_wallet_app.dtos.request.transaction_request import TransactionRequest
from e_wallet_app.dtos.response.transaction_response import TransactionResponse


class Mapper:

    def map(self, transfer: Transaction, transaction_request: TransactionRequest) -> Transaction:
        transaction_request.set_amount(transfer.get_amount())
        transaction_request.set_sender_pin(transfer.get_sender_pin())
        transaction_request.set_recipient_account_number(transfer.get_recipient_account_number())
        transaction_request.set_account_id_num(transfer.get_account_id_num())
        return transfer

    def map_transaction(self, transaction: Transaction, transaction_response: TransactionResponse) -> None:
        transaction_response.set_amount(transaction.get_amount())
        transaction_response.set_recipient_account_number(transaction.get_recipient_account_number())
