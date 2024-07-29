from classes.Account import Account
from enums.AccountTypes import AccountTypes


class CurrentAccount(Account):

    def __init__(
        self,
        password,
        branch,
        customer,
        overdraft_limit=500,
        withdrawal_limit=1000,
        transaction_limit=10,
    ) -> None:
        super().__init__(
            password, branch, customer, account_type=AccountTypes.CURRENT.value
        )
        self.__overdraft_limit = overdraft_limit
        self.__withdrawal_limit = withdrawal_limit
        self.__transaction_limit = transaction_limit
        self.account_bd = Account(
            password, branch, customer, AccountTypes.CURRENT.value
        )

    @property
    def overdraft_limit(self):
        return self.__overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, value):
        self.__overdraft_limit = value

    @property
    def withdrawal_limit(self):
        return self.__withdrawal_limit

    @withdrawal_limit.setter
    def withdrawal_limit(self, value):
        self.__withdrawal_limit = value

    @property
    def transaction_limit(self):
        return self.__transaction_limit

    @transaction_limit.setter
    def transaction_limit(self, value):
        self.__transaction_limit = value

    def to_tuple(self):
        return (
            super().id_account,
            self.overdraft_limit,
            self.withdrawal_limit,
            self.transaction_limit,
        )
