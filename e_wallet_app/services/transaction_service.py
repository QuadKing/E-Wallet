from e_wallet_app.data.repositories.transaction_repository.transaction_repository import TransactionRepository
from e_wallet_app.dtos.reponse.transaction_response import TransactionResponse
from e_wallet_app.dtos.request.transcation_request import TransactionRequest


class TransactionService:

    def get_balance_by_account_number(self, account_number: int) -> float:
        raise NotImplementedError

    def find_list_of_transaction_by_account_id(self, request: TransactionRequest) -> list[TransactionResponse]:
        raise NotImplementedError

    def find_all_transactions(self, request: TransactionRequest) -> TransactionRepository:
        raise NotImplementedError

