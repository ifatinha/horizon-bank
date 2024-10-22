from datetime import datetime
from enums.AccountTypes import AccountTypes
import random


class Account:

    def __init__(
        self, password, branch, customer, account_type=AccountTypes.BUSINESS.value
    ) -> None:
        self.__id_account = None
        self.__number = None
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

    @number.setter
    def number(self, number):
        self.__number = number

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

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    @property
    def update_at(self):
        return self.__update_at

    @update_at.setter
    def update_at(self, update_at):
        self.update_at = update_at

    @staticmethod
    def generate_account_number():
        return f"{random.randint(1000000000, 9999999999)}"

    def __str__(self) -> str:
        return (
            f"Código de registro: {self.id_account}\n"
            f"Conta: {self.number} - {self.account_type}\n"
            f"Agência: {self.branch.number}\n"
            f"Saldo: R$ {self.balance:.2f}\n"
            f"Cliente: {self.customer.fullname} - Token: {self.customer.token}"
        )

    def to_tuple(self):
        return (
            self.number,
            self.password,
            self.balance,
            self.account_type,
            self.branch.id_branch,
            self.customer.customer_id,
        )
