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
        query = f"INSERT INTO admin (user, password) VALUES(%s, %s)"
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
        query = f"SELECT * FROM admin WHERE user = %s AND password = %s"
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
        query = "INSERT INTO address(number, street, postal_code, neighborhood, city, state, country, address_type, is_primary, notes) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
        query = "SELECT number, street, postal_code, neighborhood, city, state, country, address_type, is_primary, notes from address a JOIN address_customer ac on ac.id_address = a.id JOIN customer c on c.id = ac.id_customer and c.id = %s;"

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
        query = "INSERT INTO customer(fullname, email, password, phone) VALUES(%s, %s, %s, %s)"
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
        query = "INSERT INTO manager(manager_id, employee_number, hire_date, manager_status) VALUES(%s, %s, %s, %s)"
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
    def find_manager(manager_id):
        query = "SELECT manager_id, fullname, email, password, phone, employee_number, manager_status FROM manager m JOIN customer c on m.manager_id = %s AND m.manager_id = c.id"
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
    def insert_branch(branch):
        query = "INSERT INTO branch(number, name, phone, open_date, manager_id, address_id) VALUES(%s, %s, %s, %s, %s, %s)"
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
        query = "SELECT branch_id, number, name FROM branch WHERE number = %s"

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
    def find_customer(id_customer):
        query = "SELECT id, fullname FROM customer WHERE id = %s"

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (id_customer,))
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
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")
