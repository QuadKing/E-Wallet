class TransactionRequest:
    def __init__(self):
        self.__account_id_num: int = 0
        self.__recipient_account_number: int = 0
        self.__amount: float = 0.0
        self.__sender_pin: str = ""

    def set_recipient_account_number(self, recipient_account_number: int) -> None:
        self.__recipient_account_number = recipient_account_number

    def get_recipient_account_number(self) -> int:
        return self.__recipient_account_number

    def set_amount(self, amount: float) -> None:
        self.__amount = amount

    def get_amount(self) -> float:
        return self.__amount

    def set_sender_pin(self, sender_pin: str) -> None:
        self.__sender_pin = sender_pin

    def get_sender_pin(self) -> str:
        return self.__sender_pin

    def set_account_id_num(self, account_id_num: int) -> None:
        self.__account_id_num = account_id_num

    def get_account_id_num(self) -> int:
        return self.__account_id_num
