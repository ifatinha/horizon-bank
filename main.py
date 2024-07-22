from database.DatabaseOperations import DatabaseOperations
from sql.script_create_tables import create_database, create_tables

from util.menu import (
    main_menu,
    manager_menu,
    client_menu,
    menu_type_customer,
    menu_type_account,
    menu_create_manager,
    menu_create_branch,
    menu_typle_customers,
)

from util.ReturnObjetc import (
    return_manager,
    return_branch,
    return_individual,
    return_company,
    return_account,
    return_savign_account,
    return_current_account,
    return_historic,
)


def main():

    # create_database()
    # create_tables()

    while True:

        option = main_menu()

        if option == "1":
            cl_option = client_menu()

            if cl_option == "1":
                """Cadastrar nova conta"""

            elif cl_option == "2":
                """Depositar"""

            elif cl_option == "3":
                """Sacar"""

            elif cl_option == "4":
                """Estrato"""

            elif cl_option == "5":
                """Contas Cadastradas"""

            elif cl_option == "0":
                break

            else:
                print("\n@@@ Operação inválida, selecione novamente. @@@\n")

        elif option == "2":
            user = input("Usuário: ")
            password = input("Password: ")

            status = DatabaseOperations.login_admin(user=user, password=password)

            if len(status):

                mg_option = manager_menu()

                if mg_option == "1":
                    """Cadastrar Novo Cliente"""

                    while True:
                        tp_option = menu_type_customer()

                        if tp_option == "1":
                            """Pessoa Fisica"""
                            individual = return_individual()
                            id_customer = DatabaseOperations.insert_customer(
                                individual.customer_to_tuple()
                            )
                            id_address = DatabaseOperations.insert_address(
                                individual.address
                            )
                            DatabaseOperations.insert_address_customer(
                                id_address, id_customer
                            )
                            DatabaseOperations.insert_invidual(individual, id_customer)
                        elif tp_option == "2":
                            """Pessoa Juridica"""
                            company = return_company()
                            id_customer = DatabaseOperations.insert_customer(
                                company.customer_to_tuple()
                            )
                            id_address = DatabaseOperations.insert_address(
                                company.address
                            )
                            DatabaseOperations.insert_address_customer(
                                id_address, id_customer
                            )
                            DatabaseOperations.insert_company(id_customer, company)
                        elif tp_option == "0":
                            break

                        else:
                            print("@@@ Opção inválida @@@")

                elif mg_option == "2":
                    """Cadastrar Nova Conta"""

                    while True:
                        menu_option = menu_type_account()

                        if menu_option == "1":
                            """Conta Poupança"""
                            savign_account = return_savign_account()
                            id_account = DatabaseOperations.insert_account(
                                savign_account.super_to_tuple()
                            )

                            savign_account.id_account = id_account
                            DatabaseOperations.insert_savign_account(
                                savign_account.to_tuple()
                            )

                            historic = return_historic(savign_account)
                            DatabaseOperations.insert_historic(historic)

                        elif menu_option == "2":
                            """Conta Corrente"""
                            current_account = return_current_account()
                            id_account = DatabaseOperations.insert_account(
                                current_account.super_to_tuple()
                            )
                            current_account.id_account = id_account

                            DatabaseOperations.insert_current_account(
                                current_account.to_tuple()
                            )
                            historic = return_historic(current_account)
                            DatabaseOperations.insert_historic(historic)
                        elif menu_option == "3":
                            """Conta Empresárial"""

                            account = return_account()
                            id_account = DatabaseOperations.insert_account(
                                account.to_tuple()
                            )
                            account.id_account = id_account
                            historic = return_historic(account)
                            DatabaseOperations.insert_historic(historic)
                        elif menu_option == "0":
                            break

                        else:
                            print("@@@ Opção Inválida! Tente novamente. @@@")

                elif mg_option == "3":
                    """Contas Cliente"""

                elif mg_option == "4":
                    """Listar Clientes"""

                    while True:
                        option = menu_typle_customers()

                        if option == "1":
                            print("##### PESSOAS FÍSICAS #####")
                            result = DatabaseOperations.list_individual_customers()

                            for client in result:
                                print(client + "\n")

                        elif option == "2":
                            print("##### PESSOAS JURIDICAS #####")
                            result = DatabaseOperations.list_company_customers()

                            for client in result:
                                print(client + "\n")

                        elif option == "0":
                            print("### Retornando ao menu principal. ###")
                            break
                        else:
                            print("@@@ Opção Inválida. @@@")

                elif mg_option == "5":
                    """Cadastrar Gerente"""

                    while True:
                        op_manager = menu_create_manager()

                        if op_manager == "1":
                            print(
                                "Informe os dados abaixo para cadastar um novo gerente"
                            )
                            manager = return_manager()
                            id_customer = DatabaseOperations.insert_customer(
                                manager.customer_to_tuple()
                            )
                            id_address = DatabaseOperations.insert_address(
                                manager.address
                            )
                            DatabaseOperations.insert_address_customer(
                                id_address, id_customer
                            )
                            DatabaseOperations.insert_admin(
                                manager.employee_number, manager.password
                            )
                            DatabaseOperations.insert_manager(manager, id_customer)

                        elif op_manager == "0":
                            break

                        else:
                            print("@@@ Opção Inválida! Tente novamente. @@@")

                elif mg_option == "6":
                    """Cadastrar Filial"""

                    while True:
                        op_branch = menu_create_branch()

                        if op_branch == "1":
                            branch = return_branch()
                            id_address = DatabaseOperations.insert_address(
                                branch.address
                            )
                            DatabaseOperations.insert_branch(
                                branch.to_tuple() + (id_address,)
                            )

                            DatabaseOperations.update_status_manager(
                                branch.manager.customer_id
                            )
                        elif op_branch == "0":
                            break
                        else:
                            print("@@@ Opção Inválida! Tente novamente. @@@")

                elif mg_option == "0":
                    break

                else:
                    print("\n@@@ Operação inválida, selecione novamente. @@@\n")
            else:
                print("@@@ Usuário ou senha inválidos @@@")

        elif option == "0":
            break
        else:
            print("\n@@@ Operação inválida, selecione novamente. @@@\n")


main()
