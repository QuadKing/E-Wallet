
from e_wallet_app.data.models.transaction import Transaction
from e_wallet_app.data.repositories.transaction_repository.transaction_repository import TransactionRepository
from e_wallet_app.dtos.request.transaction_request import TransactionRequest
from e_wallet_app.dtos.response.transaction_response import TransactionResponse
from e_wallet_app.services.transaction_service import TransactionService
from e_wallet_app.utils.mapper import Mapper


class TransactionServiceImpl(TransactionService):
    __transaction_repo: TransactionRepository = TransactionRepository()
    __transactions: Transaction

    def create_transaction(self, request: TransactionRequest) -> TransactionResponse:
        transaction_response: TransactionResponse = TransactionResponse()
        transactions = Transaction()
        Mapper.map_transaction(transactions, transaction_response)
        self.__transaction_repo.save(Mapper.map(transactions, request))
        return transaction_response
