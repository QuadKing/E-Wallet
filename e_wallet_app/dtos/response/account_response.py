class AccountResponse:

    def __init__(self):
        self.__name: str = ""
        self.__account_number: int = 0
        self.__password: str = ""
        self.__email_address: str = ""
        self.__balance: float = 0.0
        self.__id_num: int = 0

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_account_number(self, account_number: int) -> None:
        self.__account_number = account_number

    def get_account_number(self) -> int:
        return self.__account_number

    def set_password(self, password: str) -> None:
        self.__password = password

    def get_password(self) -> str:
        return self.__password

    def set_email_address(self, email_address: str) -> None:
        self.__email_address = email_address

    def get_email_address(self) -> str:
        return self.__email_address

    def set_id_num(self, id_num: int) -> None:
        self.__id_num = id_num

    def get_id_num(self) -> int:
        return self.__id_num

    def set_balance(self, amount: float) -> None:
        self.__balance = amount

    def get_balance(self) -> float:
        return self.__balance

    def __str__(self) -> str:
        return f"""
        Full Name : {self.__name}
        Email Address: {self.__email_address}
        Account Number : {self.__account_number}
        Account Id : {self.__id_num}

        """
