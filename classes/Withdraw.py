from classes.Transaction import Transaction
from datetime import datetime


class Withdraw(Transaction):

    def __init__(self, value) -> None:
        super().__init__()
        self.__value = value
        self.__type = self.__class__.__name__
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()

    @property
    def value(self):
        return self.__value
