from classes.Branch import Branch
from classes.Manager import Manager
from classes.Address import Address
from database.manager_db import find_manager_status
from database.branch_db import find_branch
from controller.manager_creator import ManagerCreator
from controller.address_creator import AddressCreator


class BranchCreator:

    @staticmethod
    def get_instance() -> Branch:
        """
        Solicita os dados para cadastrar uma nova agência, garantindo que o número da agência seja único.
        Retorna uma instância da classe Branch com os dados fornecidos.
        """
        number = BranchCreator._get_unique_agency_number()
        address = AddressCreator.get_instance()
        manager = BranchCreator._get_manager()
        print(f"Gerente\n\n{manager}")

        return Branch(number, address, manager)

    @staticmethod
    def _get_unique_agency_number():
        """
        Solicita ao usuário um número de agência e verifica se já existe uma agência cadastrada com esse número.
        Retorna um número de agência único.
        """

        while True:
            try:
                branch_number = int(input("Número: "))
            except ValueError:
                print("@@@ Entrada inválida. Por favor, insira um número inteiro. @@@")

            result = find_branch(branch_number)

            if result is None:
                return branch_number

            print("@@@ Já existe uma agência cadastrada com esse número. @@@")

    @staticmethod
    def _get_manager() -> Manager:
        """
        Solicita ao usuário um número de gerente e verifica se existe um gerente cadastrado com esse número.
        Retorna um gerente.
        """

        while True:

            try:
                employee_number = int(input("Número do gerente: "))
            except ValueError:
                print("@@@ Entrada inválida. Por favor, insira um número inteiro. @@@")
                continue

            record = find_manager_status(employee_number)

            if record is not None:
                return ManagerCreator.from_db_record(record)

            print("@@@ Nenhum Gerente Encontrado. Tente novamente. @@@")

    @staticmethod
    def from_db_record(record):

        address = AddressCreator.from_db_record(record)

        manager = Manager(
            record[11],
            record[12],
            None,
            record[13],
            None,
            record[14],
            record[16],
        )

        manager.customer_id = record[10]
        manager.hire_date = record[15]

        branch = Branch(record[18], address, manager)
        branch.id_branch = record[17]
        branch.name = record[19]
        branch.phone = record[20]
        branch.open_date = record[21]

        return branch
