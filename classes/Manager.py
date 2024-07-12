from classes.Customer import Customer
from datetime import datetime


class Manager(Customer):

    def __init__(self, fullname, email, telephone, address, status=True) -> None:
        super().__init__(fullname, email, telephone, address)
        self.hire_date = datetime.now()
        self.status = status

    def update(self, **kwargs):
        return super().update(**kwargs)

    def __str__(self) -> str:
        return (
            super().__str__() + f"Hire Date: {self.hire_date}\n"
            f"Status: {self.status}\n"
        )
