from datetime import datetime
from classes.Historic import Historic


class Account:

    def __init__(
        self, branch, number, password, customer, account_type="Current"
    ) -> None:
        self.__id = None
        self.__number = number
        self.__password = password
        self.__balance = float()
        self.__branch = branch
        self.__customer = customer
        self.__account_type = account_type
        self.__created_at = datetime.now()
        self.__update_at = datetime.now()

    @property
    def id(self):
        return self.__id

    @property
    def number(self):
        return self.__number

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def branch(self):
        return self.__branch

    @property
    def customer(self):
        return self.__customer

    @property
    def account_type(self):
        return self.__account_type

    @property
    def created_at(self):
        return self.__created_at

    @property
    def update_at(self):
        return self.__update_at

    def __str__(self) -> str:
        return (
            f"Conta: {self.account_number} - {self.account_type}"
            f"Agência: {self.branch}"
            f"Saldo: $ {self.balance:.2f}"
            f"Cliente: {self.customer}"
        )

    def to_tuple(self):
        return (self.number, self.password, self.balance, self.account_type)

    def withdraw(self, value):
        exceeded_balance = value > self.balance

        if exceeded_balance:
            print("@@@ Operação falhou! Você não tem saldo suficiente! @@@")
        elif value > 0:
            self.balance -= value
            print("\n=== Saque efetuado com sucesso! ===")
            return True
        else:
            print("@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def deposit(self, value):
        if value > 0:
            self.balance += value
            print("=== Depósito efetuado com sucesso! ===")
        else:
            print("@@@ Operação falhou! O valor informado é inválido! @@@")
            return False

        return True
