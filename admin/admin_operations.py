from util.menu import menu_managers, menu_branchs, menu_type_customer, menu_type_account
from controller.manager_creator import ManagerCreator
from controller.branch_creator import BranchCreator
from controller.individual_creator import IndividualCreator
from controller.company_creator import CompanyCreator
from controller.customer_creator import CustomerCreator
from controller.account_creator import AccountCreator
from database.manager_db import insert_manager, list_managers
from database.branch_db import insert_branch, list_branchs
from database.individual_db import list_individual, insert_invidual
from database.company_db import list_company, insert_company
from database.customer_db import get_valid_customer_token
from database.account_db import (
    list_accounts_customer,
    insert_business_account,
    insert_savign_account,
    insert_current_account,
)


class AdminOperations:

    @staticmethod
    def manager_customers():

        while True:

            option_manager = menu_managers()

            if option_manager == "0":
                break

            if option_manager == "1":

                manager = ManagerCreator.get_instance()
                insert_manager(manager)

            elif option_manager == "2":

                managers = list_managers()

                if managers:
                    for manager in managers:
                        print("=" * 60)
                        print(ManagerCreator.from_db_record(manager))
                        print("=" * 60 + "\n")
                else:
                    print("@@@ Nenhum gerente cadastrado. @@@")
            else:
                print("\n@@@ Operação inválida, selecione novamente. @@@\n")

    @staticmethod
    def manager_branchs():
        while True:
            option_branch = menu_branchs()

            if option_branch == "1":
                # Cadastrar nova agência
                branch = BranchCreator.get_instance()
                insert_branch(branch)

            elif option_branch == "2":
                # Listar agências cadastradas

                branchs = list_branchs()

                if branchs:
                    for branch in branchs:
                        print("=" * 60)
                        print(BranchCreator.from_db_record(branch))
                        print("=" * 60 + "\n")
                else:
                    print("@@@ Nenhuma agência encontrada. @@@")

            elif option_branch == "0":
                break
            else:
                print("\n@@@ Operação inválida, selecione novamente. @@@\n")

    @staticmethod
    def list_customers():
        while True:
            # Listar Clientes
            option = menu_type_customer()

            if option == "1":
                # Pessoas Fisicas Cadastradas
                result = list_individual()

                if result:
                    print("##### CLIENTES CADASTRADOS #####")
                    for client in result:
                        print("=" * 60)
                        print(IndividualCreator.from_db_record(client))
                        print("=" * 60 + "\n")
                else:
                    print("@@@ Nenhum cliente encontrado. @@@")

            elif option == "2":
                # Empresas Cadastradas
                result = list_company()

                if result:
                    print("##### EMPRESSAS CADASTRADAS #####")
                    for client in result:
                        print("=" * 60)
                        print(CompanyCreator.from_db_record(client))
                        print("=" * 60 + "\n")
                else:
                    print("@@@ Nenhum cliente encontrado. @@@")

            elif option == "0":
                break
            else:
                print("@@@ Opção Inválida. @@@")

    @staticmethod
    def search_customer_data():
        # Buscar dados de um cliente
        record = get_valid_customer_token()
        customer = CustomerCreator.from_db_record(record)

        accounts_customer = list_accounts_customer(customer.token)

        if accounts_customer:

            print("CONTAS DO ENCONTRADAS")
            for account in accounts_customer:
                print("=" * 60)
                print(AccountCreator.from_db_record(account))
                print("=" * 60 + "\n")

        else:
            print("@@@ O cliente não possui contas. @@@")

    @staticmethod
    def open_accounts():

        while True:
            menu_option = menu_type_account()

            if menu_option == "1":
                # Conta Poupança
                savign_account = AccountCreator.get_instance_savign_account()
                insert_savign_account(savign_account)

            elif menu_option == "2":
                # Conta Corrente
                current_account = AccountCreator.get_instance_current_account()
                insert_current_account(current_account)

            elif menu_option == "3":
                # Conta Comercial
                account = AccountCreator.get_instance_business_account()
                insert_business_account(account)

            elif menu_option == "0":
                break

            else:
                print("@@@ Opção Inválida! Tente novamente. @@@")

    @staticmethod
    def register_customers():
        while True:
            # Cadastrar Clientes
            type_customer = menu_type_customer()

            if type_customer == "1":
                # Cadastrar Pessoa Fisica
                individual = IndividualCreator.get_instance()
                insert_invidual(individual)

            elif type_customer == "2":
                # Cadastrar Pessoa Juridica
                company = CompanyCreator.get_instance()
                insert_company(company)

            elif type_customer == "0":
                # Encerrar aplicação
                break
            else:
                print("@@@ Opção inválida. Tente novamente. @@@")
