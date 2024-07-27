from connection.Connection import Connection
from database.customer_db import insert_customer
from mysql.connector import Error
from pathlib import Path
import logging


file_path = Path(__file__).resolve().parents[1] / "logs" / "mysql_logs.log"

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@staticmethod
def insert_address(address):
    query = """
            INSERT INTO address(number, street, postal_code, neighborhood, city, state, country, address_type, is_primary, notes) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    try:
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, address.to_tuple())
        conn.commit()
        logging.info("Endereço inserido no banco de dados.")
        return cursor.lastrowid
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
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (id_address, id_customer))
        conn.commit()
        logging.info("Relação Customer/Endereço inserido no banco de dados.")
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")
