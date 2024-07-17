from datetime import datetime
import random


class Account:

    def __init__(self, password, branch, customer, account_type="Current") -> None:
        self.__id_account = None
        self.__number = Account.generate_account_number()
        self.__password = password
        self.__balance = float()
        self.__branch = branch
        self.__customer = customer
        self.__account_type = account_type
        self.__created_at = datetime.now()
        self.__update_at = datetime.now()

    @property
    def id_account(self):
        return self.__id_account

    @id_account.setter
    def id_account(self, id_account):
        self.__id_account = id_account

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

    @staticmethod
    def generate_account_number():

        return f"{random.randint(1000000000, 9999999999)}"

    def __str__(self) -> str:
        return (
            f"Conta: {self.number} - {self.account_type}"
            f"\nAgência: {self.branch}"
            f"\nSaldo: $ {self.balance:.2f}"
            f"\nCliente: {self.customer}"
        )

    @staticmethod
    def return_type_account():
        accounts_type = {
            "1": "Savings",
            "2": "Current",
            "3": "Business",
        }

        return accounts_type

    def to_tuple(self):
        return (
            self.number,
            self.password,
            self.balance,
            self.account_type,
            self.branch.id_branch,
            self.customer.customer_id,
        )

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
