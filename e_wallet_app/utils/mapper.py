
def map(response: AccountResponse, account: Account) -> None:
    response.set_id_num(account.get_id_num())
    response.set_account_number(account.get_account_number())
    response.set_last_name(account.get_last_name())
    response.set_first_name(account.get_first_name())
    response.set_email_address(account.get_email_address())
