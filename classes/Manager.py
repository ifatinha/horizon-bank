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
        self.__employee_number = employee_number
        self.__hire_date = datetime.now()
        self.__status = status

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
        return super().update(**kwargs)

    def __str__(self) -> str:
        return (
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

    @staticmethod
    def generate_email(fullname):
        names = fullname.split(" ")
        if len(names) < 2:
            raise ValueError("O nome completo deve conter pelo menos dois nomes.")

        return f"{names[0].lower()}.{names[1].lower()}@horizon.com"

    @staticmethod
    def get_instance() -> "Manager":
        from database.DatabaseOperations import DatabaseOperations
        from classes.Address import Address

        print("### Dados Pessoais ###")

        while True:
            employee_number = input("Número de Registro: ")

            if not DatabaseOperations.find_manager_employee_number(employee_number):
                break
            print("@@@ Já existe um gerente com esse número. @@@")

        fullname = input("Nome Completo: ")
        password = input("Senha: ")
        phone = input("Phone: ")
        address = Address.get_instance()
        email = Manager.generate_email(fullname)

        return Manager(fullname, email, password, phone, address, employee_number)

    @staticmethod
    def from_db_record(record):
        from classes.Address import Address

        address = Address(
            record[6],
            record[7],
            record[8],
            record[9],
            record[10],
            record[11],
            record[13],
            record[15],
            record[14],
        )

        address.country = record[12]

        hire_date = record[4]
        manager = Manager(
            record[0],
            record[1],
            None,
            record[2],
            address,
            record[3],
            record[5],
        )
        manager.hire_date = hire_date

        return manager
