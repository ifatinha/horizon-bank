from classes.Individual import Individual
from datetime import datetime
from controller.address_creator import AddressCreator
from database.individual_db import find_individual_ssn


class IndividualCreator:

    @staticmethod
    def get_instance():
        """
        Solicita os dados para cadastrar uma nova pessoa, garantindo que o número de idenficação seja único.
        Retorna uma instância da classe Individual com os dados fornecidos.
        """

        print("### Dados Pessoais ###")

        ssn = IndividualCreator._get_unique_ssn_individual()
        fullname = input("Nome Completo: ")
        birth = input("Data de Nascimento (dd/mm/yyyy): ")
        birth = datetime.strptime(birth, "%d/%m/%Y")
        email = input("Email: ")
        password = input("Senha: ")
        phone = input("Telefone: ")
        address = AddressCreator.get_instance()

        return Individual(fullname, email, password, phone, address, ssn, birth)

    @staticmethod
    def _get_unique_ssn_individual() -> str:
        """
        Solicita ao usuário um número de identificação e verifica se existe uma pessoa cadastrado com esse número.
        Retorna um Individual.
        """

        while True:

            ssn = input("SSN: ")
            record = find_individual_ssn(ssn)
            if record is None:
                return ssn

            print("@@@ Já existe uma pessoa cadastrada com esse ssn. @@@")

    @staticmethod
    def from_db_record(record):
        address = AddressCreator.from_db_record(record)
        individual = Individual(
            record[10], record[11], None, record[12], address, record[13], record[14]
        )

        return individual
