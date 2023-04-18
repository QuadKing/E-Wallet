from e_wallet_app.data.repositories.transaction_repository.transaction_repository import TransactionRepository
from e_wallet_app.data.repositories.transaction_repository.transaction_repository_impl import TransactionRepositoryImpl
from e_wallet_app.services.transaction_service import TransactionService


class TransactionServiceImpl(TransactionService):

    def __init__(self):
        self.__transaction_repository: TransactionRepository = TransactionRepositoryImpl()

    def get_balance_by_account_number(self, account_number: int) -> float:
        pass

