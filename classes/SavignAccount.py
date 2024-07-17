from classes.Account import Account


class SavignAccount(Account):

    def __init__(self, password, branch, customer) -> None:
        super().__init__(password, branch, customer, account_type="Current")
        self.__interest_rate = 0.0050

    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self.__interest_rate = value

    def calculate_monthly_interest(self):
        pass

    def to_tuple(self):
        return (super().id_account, self.interest_rate)

    def super_to_tuple():
        return super().to_tuple()
