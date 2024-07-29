from util.menu import (
    manager_menu,
    menu_manager_customers,
    menu_type_customer,
    menu_managers,
    menu_branchs,
    menu_type_account,
)

from controller.manager_creator import ManagerCreator
from database.manager_db import insert_manager, list_managers
from controller.branch_creator import BranchCreator
from database.branch_db import insert_branch, list_branchs
from controller.individual_creator import IndividualCreator
from database.individual_db import insert_invidual, list_individual
from controller.company_creator import CompanyCreator
from database.company_db import insert_company, list_company
from controller.account_creator import AccountCreator
from database.account_db import (
    insert_business_account,
    insert_savign_account,
    insert_current_account,
    list_accounts_customer,
)
from controller.customer_creator import CustomerCreator
from database.customer_db import get_valid_customer_token


def admin_operations():
    while True:
        mg_option = manager_menu()

        if mg_option == "1":

            while True:

                option_customer = menu_manager_customers()

                if option_customer == "1":

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
                            print("@@@ Opção inválida @@@")

                elif option_customer == "2":
                    # Abri conta
                    while True:
                        menu_option = menu_type_account()

                        if menu_option == "1":
                            # Conta Poupança
                            savign_account = (
                                AccountCreator.get_instance_savign_account()
                            )

                            insert_savign_account(savign_account)

                        elif menu_option == "2":
                            # Conta Corrente
                            current_account = (
                                AccountCreator.get_instance_current_account()
                            )
                            insert_current_account(current_account)

                        elif menu_option == "3":
                            # Conta Comercial

                            account = AccountCreator.get_instance_business_account()
                            insert_business_account(account)

                        elif menu_option == "0":
                            break

                        else:
                            print("@@@ Opção Inválida! Tente novamente. @@@")

                elif option_customer == "3":

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
                            # Pessoas Juridicas Cadastradas

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

                elif option_customer == "4":
                    # Buscar dados de um cliente
                    record = get_valid_customer_token()
                    customer = CustomerCreator.from_db_record(record)

                    print("CONTAS DO ENCONTRADAS")

                    accounts_customer = list_accounts_customer(customer.token)

                    for account in accounts_customer:
                        print("=" * 60)
                        print(AccountCreator.from_db_record(account))
                        print("=" * 60 + "\n")

                elif option_customer == "0":
                    break
                else:
                    print("\n@@@ Operação inválida, selecione novamente. @@@\n")

        elif mg_option == "2":

            while True:
                option_manager = menu_managers()

                if option_manager == "1":

                    # Cadastrar novo gerente
                    manager = ManagerCreator.get_instance()
                    insert_manager(manager)

                elif option_manager == "2":

                    # Listar gerentes cadastrados
                    managers = list_managers()

                    if managers:
                        for manager in managers:
                            print("=" * 60)
                            print(ManagerCreator.from_db_record(manager))
                            print("=" * 60 + "\n")

                    else:
                        print("@@@ Nenhum gerente cadastrado. @@@")
                elif option_manager == "0":
                    # Retornando ao menu principal
                    break
                else:
                    print("\n@@@ Operação inválida, selecione novamente. @@@\n")

        elif mg_option == "3":
            """Gerenciamento de Agências"""

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
                    # Saindo do menu
                    break
                else:
                    print("\n@@@ Operação inválida, selecione novamente. @@@\n")

        elif mg_option == "0":
            break
        else:
            print("\n@@@ Operação inválida, selecione novamente. @@@\n")
