from database.branch_db import find_branch
from controller.branch_creator import BranchCreator
from database.customer_db import find_customer_token
from controller.customer_creator import CustomerCreator
from classes.Account import Account
from classes.SavignAccount import SavignAccount
from classes.CurrentAccount import CurrentAccount


class AccountCreator:

    @staticmethod
    def _find_branch_database():
        """
        Solicita ao usuário um número de agência e verifica se já existe uma agência cadastrada com esse número.
        Retorna objeto Branch.
        """

        while True:
            try:
                branch_number = int(input("Agência: "))
            except ValueError:
                print("@@@ Entrada inválida. Por favor, insira um número inteiro. @@@")

            result = find_branch(branch_number)

            if result:
                return result

            print("@@@ Nenhum agência encontrada para o número informado. @@@")

    @staticmethod
    def _find_individual_token():
        """
        Solicita ao usuário um token de acesso único e verifica se já existe uma pessoa cadastrada com esse número.
        Retorna objeto Individual.
        """

        while True:

            token = input("Cliente Token: ")
            result = find_customer_token(token)

            if result:
                return result

            print("@@@ Nenhum cliente encontrado para o número informado. @@@")

    @staticmethod
    def get_instance_business_account():
        print("########## ABRIR CONTA PADRÃO ##########")

        password = input("Senha: ")
        branch_record = AccountCreator._find_branch_database()
        branch = BranchCreator.from_db_record(branch_record)

        customer_record = AccountCreator._find_individual_token()
        customer = CustomerCreator.from_db_record(customer_record)

        account = Account(password, branch, customer)

        return account

    @staticmethod
    def get_instance_savign_account():
        print("########## ABRIR CONTA POUPANÇA ##########")

        password = input("Senha: ")
        branch_record = AccountCreator._find_branch_database()
        branch = BranchCreator.from_db_record(branch_record)

        customer_record = AccountCreator._find_individual_token()
        customer = CustomerCreator.from_db_record(customer_record)

        savign_account = SavignAccount(password, branch, customer)

        return savign_account

    @staticmethod
    def get_instance_current_account():
        print("########## ABRIR CONTA CORRENTE ##########")

        password = input("Senha: ")
        branch_record = AccountCreator._find_branch_database()
        branch = BranchCreator.from_db_record(branch_record)

        customer_record = AccountCreator._find_individual_token()
        customer = CustomerCreator.from_db_record(customer_record)

        current_account = CurrentAccount(password, branch, customer)

        return current_account
