from e_wallet_app.data.repositories.transaction_repository.transaction_repository import TransactionRepository
from e_wallet_app.data.repositories.transaction_repository.transaction_repository_impl import TransactionRepositoryImpl
from e_wallet_app.dtos.reponse.transaction_response import TransactionResponse
from e_wallet_app.dtos.request.transaction_request import TransactionRequest
from e_wallet_app.services.transaction_service import TransactionService


class TransactionServiceImpl(TransactionService):

    def __init__(self):
        self.__transaction_repository: TransactionRepository = TransactionRepositoryImpl()

    def get_balance_by_account_number(self, account_number: int) -> float:
        pass

    def find_list_of_transaction_by_account_id(self, request: TransactionRequest) -> list[TransactionResponse]:
        account_id_num = request.account_id_num
        transactions = self.transaction_repository.find_transactions_by_account_id(account_id_num)
        return transactions

    def find_all_transactions(self) -> list[TransactionResponse]:
        all_transaction = self.transaction_repository.get_all_transactions()
        return all_transaction

