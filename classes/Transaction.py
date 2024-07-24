from abc import ABC, abstractmethod


class Transaction(ABC):

    @property
    @abstractmethod
    def value(self):
        pass

    @abstractmethod
    def register(self, historic_id):
        pass
