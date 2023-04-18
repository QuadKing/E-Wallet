from e_wallet_app.data.models.transaction import Transaction


class TransactionRepository:

    def save(self, transaction: Transaction) -> Transaction:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError

    def find_by_id(self, id_num: int) -> Transaction:
        raise NotImplementedError

    def find_all_by_account_id(self, account_id_num: int) -> list[Transaction]:
        raise NotImplementedError

    def find_transaction_by_id(self, id_num: int) -> Transaction:
        raise NotImplementedError
