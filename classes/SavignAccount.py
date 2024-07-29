from classes.Account import Account
from enums.AccountTypes import AccountTypes


class SavignAccount(Account):

    def __init__(self, password, branch, customer) -> None:
        super().__init__(
            password, branch, customer, account_type=AccountTypes.SAVINGS.value
        )
        self.__interest_rate = 0.0050
        self.account_bd = Account(
            password, branch, customer, AccountTypes.SAVINGS.value
        )

    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self.__interest_rate = value

    def to_tuple(self):
        return (self.id_account, self.interest_rate)
