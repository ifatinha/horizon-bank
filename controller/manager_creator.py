from classes.Manager import Manager


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
        from classes.Address import Address

        address = Address(
            record[7],  # number,
            record[8],  # street,
            record[9],  # postal_code,
            record[10],  # neighborhood,
            record[11],  # city,
            record[12],  # state,
            record[14],  # address_type,
            record[13],  # country,
            record[16],  # is_primary,
            record[15],  # notes,
        )

        manager = Manager(
            record[1],
            record[2],
            None,
            record[3],
            address,
            record[4],
            record[6],
        )

        manager.customer_id = record[0]
        manager.hire_date = record[5]

        return manager
