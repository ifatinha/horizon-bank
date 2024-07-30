from database.config_db import ConfigDatabase
from connection.Connection import Connection
from database.users_db import insert_user
from sql.script_sql import (
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


class CreateDatabase:

    def __init__(self) -> None:
        self.create_database()
        self.create_tables()
        self.insert_procedures()
        self.insert_default_user()

    def create_database():
        """Criando o banco de dados, caso ele não exista"""

        Connection.check_and_create_database("horizon_Bank")

    def create_tables():
        """Criando as tabelas do banco"""
        ConfigDatabase.create_table(table_admin_query)
        ConfigDatabase.create_table(table_address_query)
        ConfigDatabase.create_table(table_customer_query)
        ConfigDatabase.create_table(table_address_customer_query)
        ConfigDatabase.create_table(table_individual_query)
        ConfigDatabase.create_table(table_company_query)
        ConfigDatabase.create_table(table_manager_query)
        ConfigDatabase.create_table(table_branch_query)
        ConfigDatabase.create_table(table_account_query)
        ConfigDatabase.create_table(table_current_account_query)
        ConfigDatabase.create_table(table_savigns_account_query)
        ConfigDatabase.create_table(table_historic_query)
        ConfigDatabase.create_table(table_transactions_query)
        ConfigDatabase.execute_sql_procedure(store_procedure_update_account_balance)
        ConfigDatabase.execute_sql_procedure(execute_automatic_procedure)

    def insert_procedures():
        """Criando as procedures"""
        ConfigDatabase.execute_sql_procedure(store_procedure_update_account_balance)
        ConfigDatabase.execute_sql_procedure(execute_automatic_procedure)

    def insert_default_user():
        insert_user("admin", "admin")
