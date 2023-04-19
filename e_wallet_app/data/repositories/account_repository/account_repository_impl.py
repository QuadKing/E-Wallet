from typing import List

from e_wallet_app.data.models.account import Account
from e_wallet_app.data.repositories.account_repository.account_repository import AccountRepository


class AccountRepositoryImpl(AccountRepository):

    def __init__(self):
        self.__accounts: list[Account] = []
        self.__count: int = 0

    def save(self, account: Account) -> Account:
        account_has_not_been_saved: bool = account.get_id_num() == 0
        if account_has_not_been_saved:
            self.save_new_account(account)
        return account

    def count(self) -> int:
        return self.__count

    def generate_id(self):
        return self.__count + 1

    def save_new_account(self, account: Account):
        account.set_id_num(self.generate_id())
        self.__accounts.append(account)
        self.__count += 1

    def find_by_id(self, id_num: int) -> Account:
        for each in self.__accounts:
            if each.get_id_num() == id_num:
                return each

    def find_by_account_number(self, account_number: int) -> Account:
        for each in self.__accounts:
            if each.get_account_number() == account_number:
                return each

    def find_all_account(self) -> list[Account]:
        return self.__accounts

    def find_by_email_address(self, email_address: str) -> Account:
        for each in self.__accounts:
            if each.get_email_address() == email_address:
                return each


