from e_wallet_app.data.models.account import Account


class AccountRepository:

    def save(self, account: Account) -> Account:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError

    def find_by_id(self, id_num: int) -> Account:
        raise NotImplementedError

    def find_by_account_number(self, account_number: int) -> Account:
        raise NotImplementedError

