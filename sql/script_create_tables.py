from database.DatabaseOperations import DatabaseOperations
from connection.Connection import Connection
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
    store_procedure_update_account_balance,
    execute_automatic_procedure,
)


def create_database():
    """Criando o banco de dados, caso ele não exista"""

    Connection.check_and_create_database("horizon_Bank")


def create_tables():
    """Criando as tabelas do banco"""
    DatabaseOperations.create_table(table_admin_query)
    DatabaseOperations.create_table(table_address_query)
    DatabaseOperations.create_table(table_customer_query)
    DatabaseOperations.create_table(table_address_customer_query)
    DatabaseOperations.create_table(table_individual_query)
    DatabaseOperations.create_table(table_company_query)
    DatabaseOperations.create_table(table_manager_query)
    DatabaseOperations.create_table(table_branch_query)
    DatabaseOperations.create_table(table_account_query)
    DatabaseOperations.create_table(table_current_account_query)
    DatabaseOperations.create_table(table_savigns_account_query)
    DatabaseOperations.create_table(table_historic_query)
    DatabaseOperations.create_table(table_transactions_query)
    DatabaseOperations.execute_sql_procedure(store_procedure_update_account_balance)
    DatabaseOperations.execute_sql_procedure(execute_automatic_procedure)


def insert_default_user():
    DatabaseOperations.insert_user("admin", "admin")
