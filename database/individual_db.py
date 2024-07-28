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


def insert_invidual(individual):
    """
    Insere um registro na tabela individual, incluindo as informações de customer e address.

    Args:
       individual (Individual): Objeto contendo as informações do customer, address e individual.

    Returns:
       None
    """

    try:
        # Inserindo o customer e recebendo o id dele
        id_customer = insert_customer(individual.customer_to_tuple())

        # Inserinto o endereço e recebento o id dele
        id_address = insert_address(individual.address)

        # Inserindo o id do customer e o id do endereço na tabela address_customer
        insert_address_customer(id_address, id_customer)

        # Inserindo dados de login
        insert_user(individual.token, individual.password)

        query = (
            "INSERT INTO individual(customer_id, ssn, date_of_birth) VALUES(%s, %s, %s)"
        )

        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, ((id_customer,) + individual.to_tuple()))
        conn.commit()

        print("### Cliente cadastrado com sucesso! ###")
        logging.info("Cliente cadastrado com sucesso.")

    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
            cursor.close()
            logging.info("Conexão fechada!")


def find_individual_ssn(ssn_number):

    try:
        query = "SELECT ssn FROM INDIVIDUAL WHERE ssn = %s"
        conn = Connection().connect()
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


def list_individual() -> list:

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
        C.fullname, 
        C.email, 
        C.phone, 
        I.ssn, 
        I.date_of_birth 
        FROM individual I
        INNER JOIN customer C
        ON C.id = I.customer_id
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
