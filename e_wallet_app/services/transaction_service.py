from e_wallet_app.dtos.request.transaction_request import TransactionRequest
from e_wallet_app.dtos.response.account_response import AccountResponse
from e_wallet_app.dtos.response.transaction_response import TransactionResponse


class TransactionService:

    def get_balance_by_account_number(self, response: AccountResponse) -> float:
        raise NotImplementedError

    def find_list_of_transaction_by_account_id(self, account_id: int) -> list[TransactionResponse]:
        raise NotImplementedError

    def find_all_transactions(self) -> list[TransactionResponse]:
        raise NotImplementedError

    def transfer(self, request: TransactionRequest) -> TransactionResponse:
        raise NotImplementedError

    def find_by_id(self, id_num: int) -> TransactionResponse:
        raise NotImplementedError

    def find_all_by_account_number(self, account_number: int) -> list[TransactionResponse]:
        raise NotImplementedError
