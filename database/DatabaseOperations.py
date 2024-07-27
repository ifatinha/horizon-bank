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
    def execute_sql_procedure(sql_procedure):
        try:
            conn = DatabaseOperations.getConnect()
            conn.connect()
            conn.cursor.execute(sql_procedure)
            logging.info("Procedure Criada!")
        except Error as err:
            logging.error(f"Erro ao criar procedure: {err}")
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
            print("### Gerente cadastrado com sucesso. ###")
            return cursor.lastrowid
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_manager(manager):
        query = """INSERT INTO manager(manager_id, employee_number, hire_date, manager_status) 
            VALUES(%s, %s, %s, %s)"""
        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, manager)
            conn.commit()
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def list_managers():
        query = """
            SELECT 
            C.fullname, 
            C.email, 
            C.phone, 
            M.employee_number, 
            M.hire_date, 
            M.manager_status, 
            A.number, 
            A.street, 
            A.postal_code, 
            A.neighborhood, 
            A.city, 
            A.state, 
            A.country, 
            A.address_type, 
            A.is_primary, 
            A.notes
            FROM customer C
            INNER JOIN 
                manager M ON C.id = M.manager_id
            INNER JOIN 
                address_customer AC ON AC.id_customer = M.manager_id
            INNER JOIN 
                address A ON A.id = AC.id_address;
            """

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
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
    def list_branchs():
        query = """
            SELECT branch_number, branch_name, phone, manager_employee_number, city, state
            FROM branch B
            INNER JOIN address A
            ON B.address_id = A.id;
            """

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_invidual(individual):
        query = (
            "INSERT INTO individual(customer_id, ssn, date_of_birth) VALUES(%s, %s, %s)"
        )

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, individual)
            conn.commit()
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_company(company):
        query = "INSERT INTO company(customer_id, ein, legal_name) VALUES(%s, %s, %s)"

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, company)
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
    def find_accounts_individual(token):
        query = """
            SELECT C.fullname, I.ssn, A.number, A.balance, A.account_type 
            FROM customer C
            INNER JOIN individual I
            ON C.id = I.customer_id
            INNER JOIN account A
            ON A.customer_id = C.id
            WHERE C.token = %s;
        """

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (token,))
            resultado = cursor.fetchall()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def find_accounts_company(token):
        query = """
            SELECT C.fullname, CO.ein, A.number, A.balance, A.account_type 
            FROM customer c
            INNER JOIN company CO
            ON C.id = CO.customer_id
            INNER JOIN account A
            ON A.customer_id = C.id
            where C.token = %s;
        """

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (token,))
            resultado = cursor.fetchall()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def find_account_customer(number, password):
        query = """
            SELECT A.number, A.balance, A.account_type 
            FROM account A WHERE A.number = %s AND A.password = %s;"""

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (number, password))
            resultado = cursor.fetchone()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def find_account_historic(account_number):
        query = """
            SELECT H.id, H.id_account
            FROM account A
            INNER JOIN historic H
            ON A.id = H.id_account
            WHERE A.number = %s;"""

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (account_number,))
            resultado = cursor.fetchone()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_deposit(account_number, value, account_balance):
        qtd_transactions_day = DatabaseOperations.number_transactions_day(
            account_number
        )

        if qtd_transactions_day[0] < 10:
            if value > 0:
                value += float(account_balance)
                query = """
                    UPDATE account A
                    SET A.balance = %s
                    WHERE A.number = %s
                """

                try:
                    conn = DatabaseOperations.getConnect().connect()
                    cursor = conn.cursor()
                    cursor.execute(query, (value, account_number))
                    conn.commit()
                    print("=== Depósito efetuado com sucesso! ===")
                    return True
                except Error as err:
                    logging.error(f"Erro ao executar SQL: {err}")
                finally:
                    if conn:
                        conn.close()
                        logging.info("Conexão fechada!")
            else:
                print("@@@ Operação falhou! O valor informado é inválido! @@@")
        else:
            print("@@@ Operação falhou! Limite de transações diárias excedido. @@@")

    @staticmethod
    def insert_transaction(transaction):
        query = """
                INSERT INTO transactions(amount, transaction_type, historic_id) 
                VALUES(%s, %s, %s)
        """

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, transaction)
            conn.commit()
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def list_historic(account_number):
        query = """
            SELECT T.amount, T.transaction_type, T.created_at 
            FROM account A
            INNER JOIN historic H
            ON A.id = H.id_account
            INNER JOIN transactions T
            ON T.historic_id = H.id
            WHERE A.number = %s"""

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (account_number,))
            resultado = cursor.fetchall()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def insert_withdraw(account_number, value, account_balance):

        qtd_transactions_day = DatabaseOperations.number_transactions_day(
            account_number
        )

        if qtd_transactions_day[0] < 10:
            exceeded_balance = value > account_balance
            if exceeded_balance:
                print("@@@ Operação falhou! Você não tem saldo suficiente! @@@")
            elif value > 0:
                if value > 0:
                    value = float(account_balance) - value
                    query = """
                        UPDATE account A
                        SET A.balance = %s
                        WHERE A.number = %s
                    """

                    try:
                        conn = DatabaseOperations.getConnect().connect()
                        cursor = conn.cursor()
                        cursor.execute(query, (value, account_number))
                        conn.commit()
                        print("\n=== Saque efetuado com sucesso! ===")
                        return True
                    except Error as err:
                        logging.error(f"Erro ao executar SQL: {err}")
                    finally:
                        if conn:
                            conn.close()
                            logging.info("Conexão fechada!")
            else:
                print("@@@ Operação falhou! O valor informado é inválido! @@@")
        else:
            print("@@@ Operação falhou! Limite de transações diárias excedido. @@@")

    @staticmethod
    def number_transactions_day(account_number):
        query = """
            SELECT COUNT(transaction_type) AS qtd_transactions
            FROM account A
            INNER JOIN historic H
            ON A.id = H.id_account
            INNER JOIN transactions T
            ON T.historic_id = H.id
            WHERE A.number = %s AND DATE(T.created_at) = CURDATE();"""

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (account_number,))
            resultado = cursor.fetchone()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def find_account(number):
        query = """
            SELECT number, balance FROM account A
            WHERE A.number = %s;"""

        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, (number,))
            resultado = cursor.fetchone()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")
