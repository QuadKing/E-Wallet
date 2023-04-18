from e_wallet_app.data.models.transaction import Transaction
from e_wallet_app.data.repositories.transaction_repository.transaction_repository import TransactionRepository


class TransactionRepositoryImpl(TransactionRepository):

    def __init__(self):
        self.__transactions: list[Transaction] = []
        self.__count: int = 0

    def save(self, transaction: Transaction) -> Transaction:
        transaction_has_not_been_saved: bool = transaction.get_id_num() == 0
        if transaction_has_not_been_saved:
            self.save_new_transaction(transaction)
        return transaction

    def count(self) -> int:
        return self.__count

    def generate_id(self):
        return self.__count + 1

    def save_new_transaction(self, transaction: Transaction):
        transaction.set_id_num(self.generate_id())
        self.__transactions.append(transaction)
        self.__count += 1

    def find_by_id(self, id_num: str) -> Transaction:
        for each in self.__transactions:
            if each.get_id_num() == id_num:
                return each

    def find_all_by_account_id(self, account_id_num: int) -> list[Transaction]:
        transactions: list[Transaction] = []
        for each in self.__transactions:
            if each.get_account_id_num() == account_id_num:
                transactions.append(each)
        return transactions

    def get_all_transactions(self) -> list[Transaction]:
        return self.__transactions
