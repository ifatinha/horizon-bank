from connection.Connection import Connection
from database.address_db import insert_address
from database.manager_db import update_status_manager
from mysql.connector import Error
from pathlib import Path
import logging


file_path = Path(__file__).resolve().parents[1] / "logs" / "mysql_logs.log"

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def find_branch(branch_number):
    """
    Verifica se existe uma agência no banco de dados com o número informado.

    Args:
        branch_number (int): Instância da classe Branch contendo os dados da agência.

    Returns:
        tupla
    """

    query = "SELECT branch_id, branch_number, branch_name FROM branch WHERE branch_number = %s"

    try:
        conn = Connection().connect()
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


def insert_branch(branch):
    """
    Insere uma nova agência no banco de dados.

    Args:
        branch (Branch): Instância da classe Branch contendo os dados da agência.

    Returns:
        None
    """

    try:
        # Inserindo dados de endereço e obtendo o ID do endereço
        id_address = insert_address(branch.address)

        # Atualiza o status do gerente para indisponível
        update_status_manager(branch.manager.employee_number)

        # Query de inserção da agência
        query = """INSERT INTO branch(branch_number, branch_name, phone, open_date, manager_employee_number, address_id) 
                VALUES(%s, %s, %s, %s, %s, %s)"""

        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (branch.to_tuple() + (id_address,)))
        conn.commit()
        print("### Agência inserida com sucesso! ###")
        logging.info("Agência inserida com sucesso!")

    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")


@staticmethod
def list_branchs():
    """
    Lista todas as agências cadastras no banco.

    Args:
        Nenhum.

    Returns:
        tupla.
    """

    query = """
            SELECT
            A.number, 
            A.street, 
            A.postal_code, 
            A.neighborhood, 
            A.city,
            A.state, 
            A.country, 
            A.address_type, 
            A.is_primary, 
            A.notes,
            C.id,
            C.fullname,
            C.email,
            C.phone, 
            M.employee_number,
            M.hire_date,
            M.manager_status,
            B.branch_number,
            B.branch_name, 
            B.phone,
            B.open_date
            FROM branch B
            INNER JOIN manager M
            ON B.manager_employee_number = M.employee_number
            INNER JOIN customer C
            ON M.manager_id = C.id
            INNER JOIN address A
            ON B.address_id = A.id;
            """

    try:
        conn = Connection().connect()
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
