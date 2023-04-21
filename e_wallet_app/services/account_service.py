<<<<<<< HEAD
from e_wallet_app.dtos.request.account_creation_request import AccountCreationRequest
=======
>>>>>>> f06bb93d9f8c7064732ae88f457a4d5ee1ff92ac
from e_wallet_app.dtos.response.account_response import AccountResponse


class AccountService:

    def create_new_account(self, account_request):
        raise NotImplementedError

    def find_all_account(self) -> list[AccountResponse]:
        raise NotImplementedError

    def find_account_by_id(self, id_num: int) -> AccountResponse:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError

    def find_by_account_number(self, account_number: int) -> AccountResponse:
        raise NotImplementedError
