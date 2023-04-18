from typing import List

from e_wallet_app.data.repositories.transaction_repository.transaction_repository import TransactionRepository
from e_wallet_app.dtos.reponse.transaction_response import TransactionResponse
from e_wallet_app.dtos.request.transaction_request import TransactionRequest
from e_wallet_app.services.transaction_service.transaction_service import TransactionService


class TransactionServiceImpl(TransactionService):
    def __init__(self, transaction_repository: TransactionRepository):
        self.transaction_repository = transaction_repository

    def find_list_of_transaction_by_account_id(self, request: TransactionRequest) -> List[TransactionResponse]:
        account_id_num = request.account_id_num
        transactions = self.transaction_repository.find_transactions_by_account_id(account_id_num)
        return transactions

    def find_all_transactions(self) -> List[TransactionResponse]:
        all_transaction = self.transaction_repository.get_all_transactions()
        return all_transaction
