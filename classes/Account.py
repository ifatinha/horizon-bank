from datetime import datetime
from classes.Historic import Historic


class Account:

    def __init__(self, branch, number, customer, account_type="Current") -> None:
        self.id = None
        self.branch = branch
        self.number = number
        self.balance = float()
        self.customer = customer
        self.account_type = account_type
        self.historic = Historic()
        self.created_at = datetime.now()
        self.update_ate = datetime.now()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
