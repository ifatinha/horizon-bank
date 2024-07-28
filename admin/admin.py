from util.menu import (
    manager_menu,
    menu_manager_customers,
    menu_type_customer,
    menu_managers,
    menu_branchs,
)

from controller.manager_creator import ManagerCreator
from database.manager_db import insert_manager, list_managers
from controller.branch_creator import BranchCreator
from database.branch_db import insert_branch, list_branchs
from controller.individual_creator import IndividualCreator
from database.individual_db import insert_invidual, list_individual


def admin_operations():
    while True:
        mg_option = manager_menu()

        if mg_option == "1":

            while True:

                option_customer = menu_manager_customers()

                if option_customer == "1":

                    while True:
                        type_customer = menu_type_customer()

                        if type_customer == "1":
                            # Cadastrar Pessoa Fisica
                            individual = IndividualCreator.get_instance()
                            insert_invidual(individual)

                        elif type_customer == "2":
                            # Cadastrar Pessoa Juridica
                            pass
                        elif type_customer == "0":
                            # Encerrar aplicação
                            break
                        else:
                            print("@@@ Opção inválida @@@")

                elif option_customer == "2":
                    """Nova Conta"""
                    #     while True:
                    #         menu_option = menu_type_account()

                    #         if menu_option == "1":
                    #             """Conta Poupança"""
                    #             savign_account = return_savign_account()
                    #             id_account = DatabaseOperations.insert_account(
                    #                 savign_account.super_to_tuple()
                    #             )

                    #             savign_account.id_account = id_account
                    #             DatabaseOperations.insert_savign_account(
                    #                 savign_account.to_tuple()
                    #             )

                    #             historic = return_historic(savign_account)
                    #             DatabaseOperations.insert_historic(historic)

                    #         elif menu_option == "2":
                    #             """Conta Corrente"""
                    #             current_account = return_current_account()
                    #             id_account = DatabaseOperations.insert_account(
                    #                 current_account.super_to_tuple()
                    #             )
                    #             current_account.id_account = id_account

                    #             DatabaseOperations.insert_current_account(
                    #                 current_account.to_tuple()
                    #             )
                    #             historic = return_historic(current_account)
                    #             DatabaseOperations.insert_historic(historic)
                    #         elif menu_option == "3":
                    #             """Conta Empresárial"""

                    #             account = return_account()
                    #             id_account = DatabaseOperations.insert_account(
                    #                 account.to_tuple()
                    #             )
                    #             account.id_account = id_account
                    #             historic = return_historic(account)
                    #             DatabaseOperations.insert_historic(historic)
                    #         elif menu_option == "0":
                    #             break

                    #         else:
                    #             print("@@@ Opção Inválida! Tente novamente. @@@")
                    pass
                elif option_customer == "3":

                    while True:
                        option = menu_type_customer()

                        if option == "1":
                            # Pessoas Fisicas Cadastradas

                            result = list_individual()

                            if result:
                                print("##### CLIENTES ENCONTRADOS #####")
                                for client in result:
                                    print("=" * 60)
                                    print(IndividualCreator.from_db_record(client))
                                    print("=" * 60 + "\n")
                            else:
                                print("@@@ Nenhum cliente encontrado. @@@")

                        elif option == "2":
                            #     print("##### CLIENTES ENCONTRADOS #####")
                            #     result = DatabaseOperations.list_company_customers()

                            #     if len(result):
                            #         for client in result:
                            #             print(client)
                            #     else:
                            #         print("@@@ Nenhum cliente encontrado. @@@")
                            pass
                        elif option == "0":
                            break
                        else:
                            print("@@@ Opção Inválida. @@@")

                elif option_customer == "4":
                    """Buscar dados de um cliente"""
                    #     """Contas Cliente"""
                    #     while True:
                    #         option = menu_type_customer()

                    #         if option == "1":
                    #             token = input("Token: ")
                    #             result = DatabaseOperations.find_accounts_individual(
                    #                 token
                    #             )

                    #             if len(result) > 0:
                    #                 print(result)
                    #             else:
                    #                 print(
                    #                     "@@@ O cliente não encontrado ou não possui contas na agência. @@@"
                    #                 )

                    #         elif option == "2":
                    #             token = input("Token: ")

                    #             result = DatabaseOperations.find_accounts_company(token)

                    #             if len(result) > 0:
                    #                 print(result)
                    #             else:
                    #                 print(
                    #                     "@@@ O cliente não encontrado ou não possui contas na agência. @@@"
                    #                 )

                    #         elif option == "0":
                    #             print("@@@ Retornando ao menu principal. @@@")
                    #             break

                    #         else:
                    #             print("@@@ Opção Inválida! @@@")
                    pass
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
                            print("====================================")
                            print(ManagerCreator.from_db_record(manager))
                            print("====================================\n")

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
                            print("==================================")
                            print(BranchCreator.from_db_record(branch))
                            print("==================================\n")
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
