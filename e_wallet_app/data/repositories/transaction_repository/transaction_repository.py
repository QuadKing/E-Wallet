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

<<<<<<< HEAD
    def get_all_transactions(self) -> list[Transaction]:
=======
    def find_all_by_account_number(self, account_number: int):
>>>>>>> 6139a369bc2a289e9c4e3bb15a5f11de7d5ea43f
        raise NotImplementedError
