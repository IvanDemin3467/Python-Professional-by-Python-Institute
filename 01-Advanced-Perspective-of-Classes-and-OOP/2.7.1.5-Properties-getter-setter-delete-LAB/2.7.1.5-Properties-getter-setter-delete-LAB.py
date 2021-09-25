class AccountException(Exception):
    pass


class BankAccount:
    def __init__(self, acc_number: int, acc_balance: int):
        self.__account_balance = acc_balance
        self.__account_init = False
        self.__account_number = acc_number

    @property
    def account_number(self) -> int:
        return self.__account_number

    @account_number.setter
    def account_number(self, amount: int) -> None:
        if self.__account_init:
            self.__account_number = amount
            self.__account_init = False
        else:
            raise AccountException("Alarm! You have no permissions to change account number!")

    @account_number.deleter
    def account_number(self) -> None:
        raise AccountException("Alarm! You have no permissions to delete account number!")

    def __del__(self):
        if self.__account_balance > 0:
            raise AccountException("You can not delete account while balance is positive")

    @property
    def account_balance(self) -> int:
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, amount: int) -> None:
        if amount < 0:
            raise AccountException("You can not set negative balance!")
        if abs(amount) > 100000:
            print("Warning! Bank operation is above 100 000.")
        self.__account_balance = amount

    @account_balance.deleter
    def account_balance(self) -> None:
        raise AccountException("Alarm! You have no permissions to delete account balance!")


if __name__ == "__main__":
    print("Creating bank account.")
    account = BankAccount(913654, 100000)
    print(f"Account number is {account.account_number}")
    print(f"Initial balance is {account.account_balance}")

    # setting the balance to 1000
    account.account_balance = 1000
    print(f"Setting account balance to {account.account_balance}. Result is OK.")

    # trying to set the balance to -200
    try:
        account.account_balance = -200
    except AccountException as e:
        print(f"Setting account balance to {-200}. Result: {str(e)}")

    # trying to set a new value for the account number
    try:
        account.account_number = 100
    except AccountException as e:
        print(f"Trying to change account number. Result: {str(e)}")
    print(f"Account number still is {account.account_number}")

    # trying to deposit 1.000.000
    print("Trying to deposit 1.000.000. Result:")
    account.account_balance += 1000000
    print(f"New account balance is {account.account_balance}")

    # trying to delete the account attribute containing a non-zero balance
    try:
        del account.account_balance
    except AccountException as e:
        print(f"Trying to delete account balance. Result: {str(e)}")

    try:
        del account.account_number
    except AccountException as e:
        print(f"Trying to delete account number. Result: {str(e)}")

    print("""Deleting account does not make sense, because garbage collector will remove it later
        Exception will be ignored and raised later.
        Lets try to change balance to 0 and delete account. No exception should be raised""")
    try:
        account.account_balance = 0
        del account
    except AccountException as e:
        print(f"Trying to delete account while balance is positive. Result: {str(e)}")

    try:
        account.account_balance = 0
    except NameError as e:
        print(f"Deletion is successful. No account presented, as you can see: {e}")
