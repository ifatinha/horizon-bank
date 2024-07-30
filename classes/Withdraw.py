from classes.Transaction import Transaction
from datetime import datetime


class Withdraw(Transaction):

    def __init__(self, value) -> None:
        super().__init__()
        self.__value = value
        self.__transaction_type = self.__class__.__name__
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        self.__updated_at = datetime.now()  # Atualiza a data de modificação

    @property
    def transaction_type(self):
        return self.__transaction_type

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at

    def to_tuple(self, historic_id):
        return (
            self.value,
            self.transaction_type,
            historic_id,
            self.created_at,
            self.updated_at,
        )
