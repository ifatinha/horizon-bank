from connection.Connection import Connection
from classes.Historic import Historic
from database.historic_db import insert_historic
from mysql.connector import Error
from pathlib import Path
import logging


file_path = Path(__file__).resolve().parents[1] / "logs" / "mysql_logs.log"

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def insert_historic_account(account):
    insert_historic(Historic(account))


def insert_business_account(account):
    """
    Insere uma nova conta empresarial no banco de dados.

    Args:
        account (Object): Um objeto contendo os valores para cadastrar um conta.

    Returns:
        int: O ID da última linha inserida, se a operação for bem-sucedida.
    """

    try:

        query = """
        INSERT INTO account(number, password, balance, account_type, branch_id, customer_id) 
        VALUES(%s, %s, %s, %s, %s, %s)"""

        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, account.to_tuple())
        conn.commit()

        # Recebendo o id da conta criada no banco de dados
        account.id_account = cursor.lastrowid

        # Criando o historico da conta
        insert_historic_account(account)

        print(f"##### A conta {account.number} foi criada. #####")
        logging.info("Conta business cadastrada no banco.")

        return cursor.lastrowid
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            cursor.close()
            logging.info("Conexão fechada!")


def insert_savign_account(savign_account):
    """
    Insere uma nova conta poupança no banco de dados.

    Args:
        savign_account (Object): Um objeto contendo os valores para cadastrar um conta poupança.

    Returns:
        int: O ID da última linha inserida, se a operação for bem-sucedida.
    """

    try:

        # Insere os dados da conta da tabela Account e recebe o id da conta inserida
        savign_account.id_account = insert_business_account(savign_account.account_bd)

        query = "INSERT INTO savigns_account(id_account, interest_rate) VALUES(%s, %s)"
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, savign_account.to_tuple())
        conn.commit()

        print("##### Tipo de conta: Poupança #####")
        logging.info("Conta poupança cadastrada no banco.")
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")
