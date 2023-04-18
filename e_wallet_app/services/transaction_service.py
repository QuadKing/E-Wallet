from e_wallet_app.dtos.request.transaction_request import TransactionRequest


class TransactionService:

    def create_transaction(self, create: TransactionRequest) -> TransactionRequest:
        raise NotImplementedError

    