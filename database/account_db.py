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
        None:
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


def insert_current_account(current_account):
    """
    Insere uma nova conta corrente no banco de dados.

    Args:
        current_account (Object): Um objeto contendo os valores para cadastrar um conta corrente.

    Returns:
        None:
    """

    try:

        # Insere os dados da conta da tabela Account e recebe o id da conta inserida
        current_account.id_account = insert_business_account(current_account.account_bd)

        query = """
            INSERT INTO current_account(id_account, overdraft_limit, withdrawal_limit, transaction_limit) 
            VALUES(%s, %s, %s, %s);
        """
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, current_account.to_tuple())
        conn.commit()

        print("##### Tipo de conta: Corrente #####")
        logging.info("Conta corrente cadastrada no banco.")
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")


def list_accounts_customer(token):
    """
    Retorna uma lista de contas associadas a um cliente específico.

    Este método aceita um token de autenticação como parâmetro e retorna uma lista de tuplas,
    onde cada tupla representa uma conta com seus detalhes.

    Parâmetros:
    token (str): O token de autenticação do cliente.

    Retorna:
    List[Tuple]: Uma lista de tuplas, onde cada tupla contém os detalhes de uma conta.
    """
    try:
        query = """
            SELECT
            B.branch_id,
            B.branch_number,
            B.branch_name,
            B.phone,
            B.open_date,
            C.id,
            C.fullname,
            C.email,
            C.token,
            C.phone,
            A.id,
            A.number,
            A.password,
            A.balance,
            A.account_type,
            A.created_at
            FROM account A
            INNER JOIN customer C
            ON C.id = A.customer_id
            INNER JOIN branch B
            ON B.branch_id = A.branch_id
            WHERE C.token = %s
        """
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (token,))
        return cursor.fetchall()

    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")


def find_account(number_account, password):
    """
    Retorna uma conta específica através de seu número e senha.

    Este método aceita um numero de conta e uma senha como parâmetro e retorna uma conta especifica.

    Parâmetros:
    number_account (int): O número da conta.
    password (str): A senha da conta.

    Retorna:
    Account[Object]: Uma conta.
    """
    try:
        query = """
            SELECT
            B.branch_id,
            B.branch_number,
            B.branch_name,
            B.phone,
            B.open_date,
            C.id,
            C.fullname,
            C.email,
            C.token,
            C.phone,
            A.id,
            A.number,
            A.password,
            A.balance,
            A.account_type,
            A.created_at
            FROM account A
            INNER JOIN customer C
            ON C.id = A.customer_id
            INNER JOIN branch B
            ON B.branch_id = A.branch_id
            WHERE A.number = %s and A.password = %s
        """
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (number_account, password))
        return cursor.fetchone()

    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")


def find_account_number(number_account):
    """
    Retorna uma conta específica através de seu número.

    Este método aceita um numero de conta e uma senha como parâmetro e retorna uma conta especifica.

    Parâmetros:
    number_account (int): O número da conta.
    password (str): A senha da conta.

    Retorna:
    Account[Object]: Uma conta. Caso contrário retorna None.
    """
    try:
        query = """
            SELECT
            B.branch_id,
            B.branch_number,
            B.branch_name,
            B.phone,
            B.open_date,
            C.id,
            C.fullname,
            C.email,
            C.token,
            C.phone,
            A.id,
            A.number,
            A.password,
            A.balance,
            A.account_type,
            A.created_at
            FROM account A
            INNER JOIN customer C
            ON C.id = A.customer_id
            INNER JOIN branch B
            ON B.branch_id = A.branch_id
            WHERE A.number = %s
        """
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (number_account,))
        return cursor.fetchone()

    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
        return None
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")


def find_balance_account(account_number):
    """
    Retorna o saldo da conta para o número de conta fornecido.

    Args:
    account_number (int): O número da conta cujo saldo deve ser retornado.

    Returns:
    float: O saldo da conta.
    """

    try:
        query = """
            SELECT
            A.balance
            FROM account A
            WHERE A.number = %s
        """
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (account_number,))
        return cursor.fetchone()

    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
        return None
    finally:
        if conn:
            conn.close()
            cursor.close()
            logging.info("Conexão fechada!")
