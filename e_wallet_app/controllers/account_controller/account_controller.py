from e_wallet_app.services.account_service_impl import AccountServiceImpl


class AccountController:
    def __init__(self):
        self.__account_service = AccountServiceImpl()

    def find_all_accounts(self):
        accounts = self.__account_service.find_all_account()
        return [account for account in accounts]

    def get_account_by_id(self, id_num):
        account = self.__account_service.find_account_by_id(id_num)
        return account

    def create_new_account(self, request):
        d_account = self.__account_service.create_new_account(request)
        return d_account

    def get_account_balance(self, account_number):
        balance = self.__account_service.find_by_account_number(account_number)
        return balance


