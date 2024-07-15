from classes.Customer import Customer
from datetime import datetime


class Manager(Customer):

    def __init__(
        self,
        fullname,
        email,
        phone,
        address,
        employee_number,
        status=True,
    ) -> None:
        super().__init__(fullname, email, phone, address)
        self.employee_number = employee_number
        self.hire_date = datetime.now()
        self.status = status

    def update(self, **kwargs):
        return super().update(**kwargs)

    def __str__(self) -> str:
        return (
            super().__str__() + f"\nHire Date: {self.hire_date}\n"
            f"Status: {self.status}\n"
        )

    def to_tuple(self):
        return (self.employee_number, self.hire_date, self.status)

    def customer_to_tuple(self):
        return super().to_tuple()
