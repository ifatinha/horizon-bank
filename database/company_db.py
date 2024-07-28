from connection.Connection import Connection
from database.customer_db import insert_customer
from database.address_db import insert_address, insert_address_customer
from database.users_db import insert_user
from mysql.connector import Error
from pathlib import Path
import logging


file_path = Path(__file__).resolve().parents[1] / "logs" / "mysql_logs.log"

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def find_company_ein(ein_number) -> tuple:
    query = "SELECT ein FROM company WHERE ein = %s"

    try:
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (ein_number,))
        resultado = cursor.fetchone()
        return resultado
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
        return None
    finally:
        if conn:
            conn.close()
            cursor.close()
            logging.info("Conexão fechada!")


def insert_company(company):
    """
    Insere uma empresa no banco de dados.

    Parâmetros:
    company (Company): Objeto que contém os dados da empresa a ser inserida.

    Returns:
       None

    """
    try:
        # Insere o customer e recebendo o id dele
        id_customer = insert_customer(company.customer_to_tuple())

        # Insere o endereço e recebento o id dele
        id_address = insert_address(company.address)

        # Insere o id do customer e o id do endereço na tabela address_customer
        insert_address_customer(id_address, id_customer)

        # Insere dados de login
        insert_user(company.token, company.password)

        query = "INSERT INTO company(customer_id, ein, legal_name) VALUES(%s, %s, %s)"

        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, ((id_customer,) + company.to_tuple()))
        conn.commit()

        print("### Empresa cadastrada com sucesso! ###")
        logging.info("Empresa cadastrada com sucesso.")

    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
            cursor.close()
            logging.info("Conexão fechada!")


def list_company() -> list:

    try:
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
        CO.ein,
        CO.legal_name
        FROM company CO
        INNER JOIN customer C
        ON C.id = CO.customer_id
        INNER JOIN address_customer AC
        ON AC.id_customer = C.id
        INNER JOIN address A
        ON A.id = AC.id_address;"""

        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query)
        record = cursor.fetchall()
        return record

    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
        return []
    finally:
        if conn:
            conn.close()
            cursor.close()
            logging.info("Conexão fechada!")
