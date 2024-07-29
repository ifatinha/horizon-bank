from database.branch_db import find_branch
from controller.branch_creator import BranchCreator
from database.customer_db import find_customer_token
from controller.customer_creator import CustomerCreator
from classes.Account import Account
from classes.Branch import Branch
from classes.Customer import Customer
from classes.SavignAccount import SavignAccount
from classes.CurrentAccount import CurrentAccount
from controller.branch_creator import BranchCreator


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
        account.number = Account.generate_account_number()

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
        savign_account.number = Account.generate_account_number()
        savign_account.account_bd.number = savign_account.number

        print(savign_account)
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
        current_account.number = Account.generate_account_number()
        current_account.account_bd.number = current_account.number

        return current_account

    @staticmethod
    def from_db_record(record):
        branch = Branch(record[1], None, None)
        branch.id_branch = record[0]
        branch.name = record[2]
        branch.phone = record[3]
        branch.open_date = record[4]

        customer = Customer(record[6], record[7], None, record[9], None)
        customer.customer_id = record[5]
        customer.token = record[8]

        account = Account(record[12], branch, customer, record[14])
        account.id_account = record[10]
        account.number = record[11]
        account.balance = record[13]
        account.created_at = record[15]

        return account
