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


@staticmethod
def insert_customer(customer):
    query = """
            INSERT INTO customer(fullname, email, password, token, phone) 
            VALUES(%s, %s, %s, %s, %s)"""
    try:
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, customer)
        conn.commit()
        logging.info("Customer inserido no banco de dados.")
        return cursor.lastrowid
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")
