from e_wallet_app.data.models.transaction import Transaction
from e_wallet_app.data.repositories.transaction_repository import transaction_repository
from e_wallet_app.data.repositories.transaction_repository.transaction_repository import TransactionRepository
from e_wallet_app.data.repositories.transaction_repository.transaction_repository_impl import TransactionRepositoryImpl
from e_wallet_app.dtos.reponse.transaction_response import TransactionResponse
from e_wallet_app.dtos.request.transaction_request import TransactionRequest
from e_wallet_app.services.transaction_service import TransactionService
from e_wallet_app.utils import mapper


class TransactionServiceImpl(TransactionService):

    def __init__(self):
        self.__transaction_repository: TransactionRepository = TransactionRepositoryImpl()

    def get_balance_by_account_number(self, account_number: int) -> float:
        pass

    def find_all_transactions(self) -> list[TransactionResponse]:
        transactions: list[Transaction] = self.__transaction_repository.get_all_transactions()
        return mapper.map_all_transactions_to_transaction_responses(transactions)

    def find_list_of_transaction_by_account_id(self: TransactionRequest) -> TransactionResponse:
        TransactionRepository.find_all_by_account_id(TransactionRequest)
        transaction = TransactionResponse()
        return transaction





