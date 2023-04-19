from e_wallet_app.data.models.account import Account
from e_wallet_app.data.models.transaction import Transaction
from e_wallet_app.data.repositories.account_repository.account_repository import AccountRepository
from e_wallet_app.data.repositories.transaction_repository.transaction_repository import TransactionRepository
from e_wallet_app.data.repositories.transaction_repository.transaction_repository_impl import TransactionRepositoryImpl
from e_wallet_app.dtos.request.transaction_request import TransactionRequest
from e_wallet_app.dtos.response.account_response import AccountResponse
from e_wallet_app.dtos.response.transaction_response import TransactionResponse
from e_wallet_app.exceptions.account_does_not_exist_exception import AccountDoesNotExistException
from e_wallet_app.exceptions.insufficient_fund_exception import InsufficientFundException
from e_wallet_app.exceptions.invalid_amount_exception import InvalidAmountException
from e_wallet_app.exceptions.invalid_credential_exception import InvalidCredentialException
from e_wallet_app.services.transaction_service import TransactionService
from e_wallet_app.utils import mapper


class TransactionServiceImpl(TransactionService):
    def __init__(self):
        self.WALLET_ID = 0
        self.__transaction_repository: TransactionRepository = TransactionRepositoryImpl()
        self.__account_repository: AccountRepository = AccountRepository()

    def get_balance_by_account_number(self, response: AccountResponse) -> float:
        return self.calculate_balance(response.get_id_num(), response.get_account_number())

    def transfer(self, request: TransactionRequest) -> TransactionResponse:
        self.validate(request)
        transaction: Transaction = self.__transaction_repository.save(mapper.map_transaction_request_to_transaction(request))
        return mapper.map_transaction_to_transaction_response(transaction)

    def validate(self, request):
        if request.get_account_id_num() != self.WALLET_ID:
            self.validate_account_existence(request)
        self.validate_amount(request)
        self.validate_pin(request)

    def validate_account_existence(self, request):
        sender_account: Account = self.__account_repository.find_by_id(request.get_account_id_num())
        recipient_account: Account = self.__account_repository.find_by_account_number(request.get_recipient_account_number())
        if sender_account is None or recipient_account is None:
            raise AccountDoesNotExistException()

    def validate_amount(self, request: TransactionRequest):
        self.validate_negative_amount(request.get_amount())
        if request.get_account_id_num() != self.WALLET_ID:
            self.validate_insufficient_amount(request)

    def validate_negative_amount(self, amount):
        if amount < 0:
            raise InvalidAmountException()

    def validate_insufficient_amount(self, request: TransactionRequest):
        account: Account = self.__account_repository.find_by_id(request.get_account_id_num())
        current_balance: float = self.calculate_balance(account.get_id_num(), account.get_account_number())
        if current_balance < request.get_amount():
            raise InsufficientFundException()

    def calculate_sum(self, transactions: list[Transaction]):
        sums: float = 0.0
        for each in transactions:
            sums += each.get_amount()
        return sums

    def validate_pin(self, request):
        if request.get_account_id_num() != self.WALLET_ID:
            if self.__account_repository.find_by_id(request.get_account_id_num()).get_pin() != request.get_sender_pin():
                raise InvalidCredentialException()

    def calculate_balance(self, sender_id, recipient_account_number):
        debit_transactions: list[Transaction] = self.__transaction_repository.find_all_by_account_id(sender_id)
        withdrawal_sum: float = self.calculate_sum(debit_transactions)
        credit_transactions: list[Transaction] = self.__transaction_repository.find_all_by_account_number(recipient_account_number)
        credit_sum: float = self.calculate_sum(credit_transactions)
        return credit_sum - withdrawal_sum

