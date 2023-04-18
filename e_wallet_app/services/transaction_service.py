<<<<<<< HEAD
from e_wallet_app.data.repositories.transaction_repository.transaction_repository import TransactionRepository
from e_wallet_app.dtos.reponse.transaction_response import TransactionResponse
from e_wallet_app.dtos.request.transcation_request import TransactionRequest
=======
from e_wallet_app.dtos.request.transaction_request import TransactionRequest
from e_wallet_app.dtos.response.account_response import AccountResponse
from e_wallet_app.dtos.response.transaction_response import TransactionResponse
>>>>>>> 6139a369bc2a289e9c4e3bb15a5f11de7d5ea43f


class TransactionService:

    def get_balance_by_account_number(self, response: AccountResponse) -> float:
        raise NotImplementedError

<<<<<<< HEAD
    def find_list_of_transaction_by_account_id(self, request: TransactionRequest) -> list[TransactionResponse]:
        raise NotImplementedError

    def find_all_transactions(self, request: TransactionRequest) -> TransactionRepository:
        raise NotImplementedError

=======
    def transfer(self, request: TransactionRequest) -> TransactionResponse:
        raise NotImplementedError
>>>>>>> 6139a369bc2a289e9c4e3bb15a5f11de7d5ea43f
