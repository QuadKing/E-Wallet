class TransactionResponse:
    def __init__(self):
        self.__id_num: int = 0
        self.__account_id_num: int = 0
        self.__recipient_account_number: str = ""
        self.__amount: float = 0.0

    def set_recipient_account_number(self, recipient_account_number: str) -> None:
        self.__recipient_account_number = recipient_account_number

    def get_recipient_account_number(self) -> str:
        return self.__recipient_account_number

    def set_amount(self, amount: float) -> None:
        self.__amount = amount

    def get_amount(self) -> float:
        return self.__amount

    def get_id_num(self) -> int:
        return self.__id_num

    def set_account_id_num(self, account_id_num: int) -> None:
        self.__account_id_num = account_id_num

    def get_account_id_num(self) -> int:
        return self.__account_id_num


