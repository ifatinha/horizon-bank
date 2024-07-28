from classes.Company import Company
from datetime import datetime
from controller.address_creator import AddressCreator
from database.company_db import find_company_ein


class CompanyCreator:

    @staticmethod
    def get_instance():
        """
        Solicita os dados para cadastrar uma nova empresa, garantindo que o número de idenficação seja único.
        Retorna uma instância da classe Company com os dados fornecidos.
        """

        ein = CompanyCreator._get_unique_ein_company()
        fullname = input("Razão Social: ")
        legal_name = input("Nome Fantasia: ")
        email = input("Email: ")
        password = input("Senha: ")
        phone = input("Telefone: ")
        address = AddressCreator.get_instance()

        return Company(fullname, email, password, phone, address, ein, legal_name)

    @staticmethod
    def _get_unique_ein_company() -> str:
        """
        Solicita ao usuário um número de identificação e verifica se existe uma empresa cadastrada com esse número.
        Retorna um ein válido.
        """

        while True:

            ein = input("EIN: ")
            record = find_company_ein(ein)
            if record is None:
                return ein

            print("@@@ Já existe uma empresa cadastrada com o ein informado. @@@")

    @staticmethod
    def from_db_record(record):
        address = AddressCreator.from_db_record(record)
        company = Company(
            record[10], record[11], None, record[12], address, record[13], record[14]
        )
        return company
