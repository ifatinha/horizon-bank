from classes.Account import Account


class SavignAccount(Account):

    def __init__(self, branch, number, customer, account_type="Current") -> None:
        super().__init__(branch, number, customer, account_type)
        self.__interest_rate = 0.005

    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self.__interest_rate = value

    def calculate_monthly_interest(self):
        pass