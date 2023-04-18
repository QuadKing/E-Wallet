from e_wallet_app.data.models.transaction import Transaction


class TransactionRepository:

    def __init__(self):
        self.Transaction = None

    def save(self, transaction: Transaction) -> Transaction:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError

    def find_by_id(self, id_num: int) -> Transaction:
        raise NotImplementedError

    def find_all_by_account_id(self, account_id_num: int) -> list[Transaction]:
        raise NotImplementedError

    def get_all_transactions(self) -> list[Transaction]:
        raise NotImplementedError
