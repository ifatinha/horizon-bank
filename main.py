from database.DatabaseOperations import DatabaseOperations
from connection.Connection import Connection
from util.menu import main_menu, manager_menu, client_menu
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

from util.ReturnObjetc import return_manager, return_branch

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

            status = DatabaseOperations.login_admin(user=user, passowrd=password)

            if len(status):

                mg_option = manager_menu()

                if mg_option == "1":
                    """Cadastrar Novo Cliente"""

                elif mg_option == "2":
                    """Cadastrar Nova Conta"""

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
                    DatabaseOperations.insert_manager(manager, id_customer)
                    DatabaseOperations.insert_address_customer(id_address, id_customer)

                elif mg_option == "7":
                    """Cadastrar Filial"""
                    return_branch()
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
