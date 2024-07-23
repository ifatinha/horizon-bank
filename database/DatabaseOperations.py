from connection.Connection import Connection
from mysql.connector import Error
from pathlib import Path
import mysql.connector
import mysql.connector.errorcode
import logging

# Configuração básica do logging para registrar em um arquivo
file_path = Path(__file__).resolve().parents[1] / "logs" / "mysql_logs.log"

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class DatabaseOperations:

    @staticmethod
    def getConnect():
        conn = Connection()
        return conn

    @staticmethod
    def create_table(table_creation_query):
        try:
            conn = DatabaseOperations.getConnect()
            conn.connect()
            conn.cursor.execute(table_creation_query)
            logging.info("Tabela Criada!")
        except Error as err:
            logging.error(f"Erro ao criar a tabela: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_admin(user, password):
        query = f"INSERT INTO admin (token, password) VALUES(%s, %s)"
        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (user, password))
            conn.commit()
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def login_admin(user, password):
        query = f"SELECT * FROM admin WHERE token = %s AND password = %s"
        try:
            conn = DatabaseOperations.getConnect()
            conn.connect()
            conn.cursor.execute(query, (user, password))
            resultado = conn.cursor.fetchall()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_address(address):
        query = """
            INSERT INTO address(number, street, postal_code, neighborhood, city, state, country, address_type, is_primary, notes) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, address.to_tuple())
            conn.commit()
            return cursor.lastrowid
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def find_address(manager_id):
        query = """SELECT number, street, postal_code, neighborhood, city, state, country, address_type, is_primary, notes 
                FROM address a 
                JOIN address_customer ac 
                ON ac.id_address = a.id 
                JOIN customer 
                c ON c.id = ac.id_customer AND c.id = %s;"""

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (manager_id,))
            resultado = cursor.fetchone()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_customer(customer):
        query = """
            INSERT INTO customer(fullname, email, password, token, phone) 
            VALUES(%s, %s, %s, %s, %s)"""
        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, customer)
            conn.commit()
            return cursor.lastrowid
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_manager(manager, manager_id):
        query = """INSERT INTO manager(manager_id, employee_number, hire_date, manager_status) 
            VALUES(%s, %s, %s, %s)"""
        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, ((manager_id,) + manager.to_tuple()))
            conn.commit()
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_address_customer(id_address, id_customer):
        query = "INSERT INTO address_customer(id_address, id_customer) VALUES(%s, %s)"
        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (id_address, id_customer))
            conn.commit()
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def find_manager_status(employee_number):
        query = """SELECT C.id, C.fullname, M.employee_number, M.manager_status 
                FROM customer C 
                JOIN manager M ON C.ID = M.manager_id 
                WHERE M.employee_number = %s AND M.manager_status = TRUE"""
        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (employee_number,))
            resultado = cursor.fetchone()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_branch(branch):
        query = """INSERT INTO branch(branch_number, branch_name, phone, open_date, manager_employee_number, address_id) 
                VALUES(%s, %s, %s, %s, %s, %s)"""
        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, branch)
            conn.commit()
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_invidual(individual, id_customer):
        query = (
            "INSERT INTO individual(customer_id, ssn, date_of_birth) VALUES(%s, %s, %s)"
        )

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, ((id_customer,) + individual.to_tuple()))
            conn.commit()
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_company(id_customer, company):
        query = "INSERT INTO company(customer_id, ein, legal_name) VALUES(%s, %s, %s)"

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, ((id_customer,) + company.to_tuple()))
            conn.commit()
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def find_branch(branch_number):
        query = "SELECT branch_id, branch_number, branch_name FROM branch WHERE branch_number = %s"

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (branch_number,))
            resultado = cursor.fetchone()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def find_customer_token(token):
        query = "SELECT id, fullname, token FROM customer WHERE token = %s"

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (token,))
            resultado = cursor.fetchone()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_account(account):
        query = "INSERT INTO account(number, password, balance, account_type, branch_id, customer_id) VALUES(%s, %s, %s, %s, %s, %s)"

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, account)
            conn.commit()
            return cursor.lastrowid
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_savign_account(savign_account):
        query = "INSERT INTO savigns_account(id, interest_rate) VALUES(%s, %s)"

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, savign_account)
            conn.commit()
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_current_account(current_account):
        query = "INSERT INTO current_account(id, overdraft_limit, withdrawal_limit, transaction_limit) VALUES(%s, %s, %s, %s)"

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, current_account)
            conn.commit()
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_historic(historic):
        query = "INSERT INTO historic(id_account) VALUES(%s)"

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, historic.to_tuple())
            conn.commit()
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def update_status_manager(manager_id):
        query = "UPDATE manager SET manager_status = False where manager_id = %s"

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (manager_id,))
            conn.commit()
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def find_manager_employee_number(employee_number):
        query = (
            "SELECT manager_id, employee_number FROM manager WHERE employee_number = %s"
        )

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (employee_number,))
            resultado = cursor.fetchone()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def find_individual_ssn(ssn_number):
        query = "SELECT ssn FROM INDIVIDUAL WHERE ssn = %s"

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (ssn_number,))
            resultado = cursor.fetchone()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def find_company_ein(ein_number):
        query = "SELECT ein FROM company WHERE ein = %s"

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (ein_number,))
            resultado = cursor.fetchone()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def list_individual_customers():
        query = """
            SELECT c.fullname, c.email, c.phone, i.ssn, i.date_of_birth, a.street, a.number, a.neighborhood, a.postal_code, a.city, a.state, a.country, a.address_type 
            FROM customer c
            INNER JOIN individual i
            on c.id = i.customer_id
            INNER JOIN address_customer ad
            on ad.id_customer = c.id
            INNER JOIN address a
            on a.id = ad.id_address;
        """

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def list_company_customers():
        query = """
            SELECT c.fullname, c.email, c.phone, co.ein, co.legal_name, a.street, a.number, a.neighborhood, a.postal_code, a.city, a.state, a.country, a.address_type FROM customer c
            INNER JOIN company co
            on c.id = co.customer_id
            INNER JOIN address_customer ad
            on ad.id_customer = c.id
            INNER JOIN address a
            on a.id = ad.id_address;
        """

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def find_accounts_individual(ssn):
        query = """
            SELECT customer.fullname, individual.ssn, account.number as 'Account number', account.account_type 
            FROM customer
            INNER JOIN individual
            ON customer.id = individual.customer_id
            INNER JOIN account
            ON account.customer_id = customer.id
            WHERE individual.ssn = %s;
        """

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (ssn,))
            resultado = cursor.fetchall()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def find_accounts_company(ein):
        query = """
            SELECT customer.fullname, company.ein, account.number as 'Account number', account.account_type 
            FROM customer
            INNER JOIN company
            ON customer.id = company.customer_id
            INNER JOIN account
            ON account.customer_id = customer.id
            where company.ein = %s;
        """

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (ein,))
            resultado = cursor.fetchall()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def login_customer(user, password):
        query = (
            f"SELECT email, password FROM customer WHERE email = %s and password = %s"
        )
        try:
            conn = DatabaseOperations.getConnect()
            conn.connect()
            conn.cursor.execute(query, (user, password))
            resultado = conn.cursor.fetchall()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")
