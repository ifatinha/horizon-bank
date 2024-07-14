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

"""Criando o banco de dados, caso ele não exista"""
# Connection.check_and_create_database("horizon_Bank")

"""Criando as tabelas do banco"""
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

        elif option == "2":
            mg_option = manager_menu()

        elif option == "0":
            break
        else:
            print("\n@@@ Operação inválida, selecione novamente. @@@\n")


main()
