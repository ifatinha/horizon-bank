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
