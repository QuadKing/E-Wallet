class AccountResponse:

    def __init__(self):
        self.__id_num: int = 0
        self.__first_name: str = ""
        self.__last_name: str = ""
        self.__account_number: int = 0
        self.__password: str = ""
        self.__email_address: str = ""

    def set_first_name(self, first_name: str) -> None:
        self.__first_name = first_name

    def get_first_name(self) -> str:
        return self.__first_name

    def set_last_name(self, last_name: str) -> None:
        self.__last_name = last_name

    def get_last_name(self) -> str:
        return self.__last_name

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