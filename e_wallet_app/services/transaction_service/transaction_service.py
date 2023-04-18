from typing import List

from e_wallet_app.data.repositories.transaction_repository.transaction_repository import TransactionRepository
from e_wallet_app.dtos.reponse.transaction_response import TransactionResponse
from e_wallet_app.dtos.request.transaction_request import TransactionRequest


class TransactionService:
    def find_list_of_transaction_by_account_id(self, request: TransactionRequest) -> List[TransactionResponse]:
        raise NotImplementedError

    def find_all_transactions(self, request: TransactionRequest) -> TransactionRepository:
        raise NotImplementedError


