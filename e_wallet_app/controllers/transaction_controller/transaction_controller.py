import json
from datetime import date, datetime
from decimal import Decimal
from urllib import request

from e_wallet_app.dtos.request.transaction_request import TransactionRequest
from e_wallet_app.dtos.response.account_response import AccountResponse
from e_wallet_app.dtos.response.transaction_response import TransactionResponse
from e_wallet_app.exceptions.account_does_not_exist_exception import AccountDoesNotExistException
from e_wallet_app.exceptions.insufficient_fund_exception import InsufficientFundException
from e_wallet_app.exceptions.invalid_amount_exception import InvalidAmountException
from e_wallet_app.exceptions.invalid_credential_exception import InvalidCredentialException
from e_wallet_app.services.transaction_service_impl import TransactionServiceImpl

transaction_service = TransactionServiceImpl()


def get_balance():
    request_data = request.json
    account_number = request_data['account_number']
    account_id_num = request_data['account_id_num']
    account_response = AccountResponse(account_id_num, account_number)
    balance = transaction_service.get_balance_by_account_number(account_response)
    return jsonify({'balance': balance})


def jsonify(data):
    def convert(obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return float(obj)
        else:
            return obj

    return json.dumps(data, default=convert)


def transfer():
    request_data = request.json
    sender_id_num = request_data['sender_id_num']
    sender_account_number = request_data['sender_account_number']
    recipient_account_number = request_data['recipient_account_number']
    amount = request_data['amount']
    sender_pin = request_data['sender_pin']
    transaction_request = TransactionRequest(sender_id_num, sender_account_number,
                                             recipient_account_number, amount, sender_pin)
    try:
        transaction_response = transaction_service.transfer(transaction_request)
        return jsonify(transaction_response.to_dict())
    except InvalidAmountException:
        return jsonify({'message': 'Invalid amount.'}), 400
    except InsufficientFundException:
        return jsonify({'message': 'Insufficient fund.'}), 400
    except InvalidCredentialException:
        return jsonify({'message': 'Invalid credentials.'}), 401
    except AccountDoesNotExistException:
        return jsonify({'message': 'Account does not exist.'}), 404


def get_transactions():
    transactions = transaction_service.find_all_transactions()
    transaction_dicts = [transaction.to_dict() for transaction in transactions]
    return jsonify({'transactions': transaction_dicts})


def get_transaction_by_id(id_num):
    try:
        transaction = transaction_service.find_by_id(id_num)
        return jsonify(transaction.to_dict())
    except AttributeError:
        return jsonify({'message': 'Transaction not found.'}), 404


def get_transactions_by_account_number(account_number):
    transactions = transaction_service.find_all_by_account_number(account_number)
    transaction_dicts = [transaction.to_dict() for transaction in transactions]
    return jsonify({'transactions': transaction_dicts})
