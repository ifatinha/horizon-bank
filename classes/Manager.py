from classes.Customer import Customer
from datetime import datetime


class Manager(Customer):

    def __init__(
        self,
        fullname,
        email,
        password,
        phone,
        address,
        employee_number,
        status=True,
    ) -> None:
        super().__init__(fullname, email, password, phone, address)
        self.employee_number = employee_number
        self.hire_date = datetime.now()
        self.status = status

    @property
    def employee_number(self):
        return self.__employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        self.__employee_number = employee_number

    @property
    def hire_date(self):
        return self.__hire_date

    @hire_date.setter
    def hire_date(self, hire_date):
        self.__hire_date = hire_date

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def update(self, **kwargs):
        super().update(**kwargs)
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        return (
            f"Gerente: {self.customer_id}\n"
            f"Nome: {self.fullname}\n"
            f"Email: {self.email}\n"
            f"Telefone: {self.phone}\n"
            f"Matricula: {self.employee_number}\n"
            f"Data de admissão: {self.hire_date}\n"
            f"Status: {'Ativo' if self.status else 'Inativo'}\n"
            f"{self.address}"
        )

    def to_tuple(self) -> tuple:
        return (self.employee_number, self.hire_date, self.status)

    def customer_to_tuple(self) -> tuple:
        return super().to_tuple()
