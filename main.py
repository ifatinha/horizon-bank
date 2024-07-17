from database.DatabaseOperations import DatabaseOperations
from connection.Connection import Connection
from util.menu import (
    main_menu,
    manager_menu,
    client_menu,
    menu_type_customer,
    menu_type_account,
)
from sql.scriptSql import (
    table_admin_query,
    table_address_query,
    table_customer_query,
    table_address_customer_query,
    table_individual_query,
    table_company_query,
    table_manager_query,
    table_branch_query,
    table_account_query,
    table_savigns_account_query,
    table_current_account_query,
    table_historic_query,
    table_transactions_query,
)

from util.ReturnObjetc import (
    return_manager,
    return_branch,
    return_individual,
    return_company,
    return_account,
)

# """Criando o banco de dados, caso ele não exista"""
# Connection.check_and_create_database("horizon_Bank")

# """Criando as tabelas do banco"""
# DatabaseOperations.create_table(table_admin_query)
# DatabaseOperations.create_table(table_address_query)
# DatabaseOperations.create_table(table_customer_query)
# DatabaseOperations.create_table(table_address_customer_query)
# DatabaseOperations.create_table(table_individual_query)
# DatabaseOperations.create_table(table_company_query)
# DatabaseOperations.create_table(table_manager_query)
# DatabaseOperations.create_table(table_branch_query)
# DatabaseOperations.create_table(table_account_query)
# DatabaseOperations.create_table(table_current_account_query)
# DatabaseOperations.create_table(table_savigns_account_query)
# DatabaseOperations.create_table(table_historic_query)
# DatabaseOperations.create_table(table_transactions_query)


def main():

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
                        account_type = ""
                        if menu_option == "1":
                            """Conta Poupança"""
                            account_type = "Savings"

                        elif menu_option == "2":
                            """Conta Corrente"""
                            account_type = "Current"

                        elif menu_option == "3":
                            """Conta Empresárial"""
                            account_type = "Business"

                        elif menu_option == "0":
                            break

                        else:
                            print("@@@ Opção Inválida! Tente novamente. @@@")

                        account = return_account(account_type)
                        id_account = DatabaseOperations.insert_account(account)

                elif mg_option == "3":
                    """Listar Contas Cadastradas"""

                elif mg_option == "4":
                    """Listar Contas do Banco"""

                elif mg_option == "5":
                    """Listar Clientes"""

                elif mg_option == "6":
                    """Cadastrar Gerente"""

                    print("Informe os dados abaixo para cadastar um novo gerente")
                    manager = return_manager()
                    id_customer = DatabaseOperations.insert_customer(
                        manager.customer_to_tuple()
                    )
                    id_address = DatabaseOperations.insert_address(manager.address)
                    DatabaseOperations.insert_address_customer(id_address, id_customer)
                    DatabaseOperations.insert_admin(
                        manager.employee_number, manager.password
                    )
                    DatabaseOperations.insert_manager(manager, id_customer)
                elif mg_option == "7":
                    """Cadastrar Filial"""
                    branch = return_branch()
                    id_address = DatabaseOperations.insert_address(branch.address)
                    DatabaseOperations.insert_branch(branch.to_tuple() + (id_address,))
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
