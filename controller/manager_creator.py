from classes.Manager import Manager
from controller.address_creator import AddressCreator


class ManagerCreator:

    @staticmethod
    def generate_email(fullname):
        names = fullname.split(" ")
        if len(names) < 2:
            raise ValueError("O nome completo deve conter pelo menos dois nomes.")

        return f"{names[0].lower()}.{names[1].lower()}@horizon.com"

    @staticmethod
    def get_instance() -> "Manager":
        from database.manager_db import find_manager_employee_number
        from controller.address_creator import AddressCreator

        print("Informe os dados abaixo para cadastar um novo gerente")
        print("### Dados Pessoais ###")

        while True:
            employee_number = input("Número de Registro: ")

            if not find_manager_employee_number(employee_number):
                break
            print("@@@ Já existe um gerente com esse número. @@@")

        fullname = input("Nome Completo: ")
        password = input("Senha: ")
        phone = input("Phone: ")
        address = AddressCreator.get_instance()
        email = ManagerCreator.generate_email(fullname)

        return Manager(fullname, email, password, phone, address, employee_number)

    @staticmethod
    def from_db_record(record):

        address = AddressCreator.from_db_record(record)

        manager = Manager(
            record[11],
            record[12],
            None,
            record[13],
            address,
            record[14],
            record[16],
        )

        manager.customer_id = record[10]
        manager.hire_date = record[15]

        return manager
