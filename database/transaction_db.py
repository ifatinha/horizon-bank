from connection.Connection import Connection
from mysql.connector import Error
from pathlib import Path
import logging


file_path = Path(__file__).resolve().parents[1] / "logs" / "mysql_logs.log"

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def insert_deposit(account_number, value, account_balance):
    """
    Insere um depósito na conta especificada.

    :param account_number: Número da conta.
    :param value: Valor do depósito.
    :param account_balance: Saldo atual da conta.
    :return: True se o depósito foi efetuado com sucesso, False caso contrário.

    """

    qtd_transactions_day = number_transactions_day(account_number)

    if qtd_transactions_day >= 10:
        print("@@@ Operação falhou! Limite de transações diárias excedido. @@@")
        return False

    if value <= 0:
        print("@@@ Operação falhou! O valor informado é inválido! @@@")
        return False

    new_balance = float(account_balance) + value

    query = """
        UPDATE account A
        SET A.balance = %s
        WHERE A.number = %s
        """

    try:
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (new_balance, account_number))
        conn.commit()

        logging.info("Deposito efetuado com sucesso!")
        return True
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")


def insert_withdraw(account_number, value, account_balance):
    """
    Faz um saque na conta especificada.

    :param account_number: Número da conta.
    :param value: Valor do depósito.
    :param account_balance: Saldo atual da conta.
    :return: True se o depósito foi efetuado com sucesso, False caso contrário.
    """

    qtd_transactions_day = number_transactions_day(account_number)

    if qtd_transactions_day >= 10:
        print("@@@ Operação falhou! Limite de transações diárias excedido. @@@")
        return False

    if value <= 0:
        print("@@@ Operação falhou! O valor informado é inválido! @@@")
        return False

    if value > account_balance:
        print("@@@ Operação falhou! Você não tem saldo suficiente! @@@")
        return False

    new_balance = float(account_balance) - value

    query = """
        UPDATE account A
        SET A.balance = %s
        WHERE A.number = %s
        """

    try:
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (new_balance, account_number))
        conn.commit()

        logging.info("Saque efetuado com sucesso!")
        return True
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
        return False
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")


def insert_transaction(transaction):
    """
    Insere uma nova transação na tabela de transações do banco de dados.

    Parâmetros:
    transaction (tuple): Uma tupla contendo os valores da transação a serem inseridos.
                         A tupla deve ter a seguinte estrutura:
                         (amount, transaction_type, historic_id, created_at, updated_at)

    Retorna:
     None
    """

    try:
        query = """
                INSERT INTO transactions(amount, transaction_type, historic_id, created_at, updated_at) 
                VALUES(%s, %s, %s, %s, %s)
         """
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, transaction)
        conn.commit()
        logging.info("Transação inserida com sucesso.")

        return True
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
        return False

    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")


def number_transactions_day(account_number) -> int:
    """
    Conta o número de transações do dia para uma conta específica.

    Parâmetros:
    account_number (int): O número da conta para a qual as transações serão contadas.

    Retorna:
    int: O número total de transações realizadas no dia para a conta especificada.
    """

    query = """
            SELECT COUNT(transaction_type) AS qtd_transactions
            FROM account A
            INNER JOIN historic H
            ON A.id = H.id_account
            INNER JOIN transactions T
            ON T.historic_id = H.id
            WHERE A.number = %s AND DATE(T.created_at) = CURDATE();"""

    try:

        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (account_number,))
        result = cursor.fetchone()

        return result[0] if result else 0

    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
        return None
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")


def list_transactions_account(account_number):
    """
    Lista todas as transações de uma conta específica.

    :param account_number: Número da conta para a qual as transações serão listadas.

    :return: Uma lista de tuplas contendo informações das transações ou None se houver erro.
    """

    query = """
            SELECT T.amount, T.transaction_type, T.created_at 
            FROM historic H
            INNER JOIN account A
            ON A.id = H.id_account
            INNER JOIN transactions T
            ON T.historic_id = H.id
            WHERE A.number = %s"""

    try:

        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (account_number,))
        return cursor.fetchall()

    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
        return None
    finally:
        if conn:
            conn.close()
            cursor.close()
            logging.info("Conexão fechada!")
