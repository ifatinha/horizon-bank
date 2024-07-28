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


def find_customer_token(token):
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
        C.token
        FROM customer C
        INNER JOIN address_customer AC
        ON AC.id_customer = C.id
        INNER JOIN address A
        ON A.id = AC.id_address
        WHERE C.token = %s AND instr(email, 'horizon') = 0;"""

        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (token,))
        record = cursor.fetchone()
        return record

    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
        return []
    finally:
        if conn:
            conn.close()
            cursor.close()
            logging.info("Conexão fechada!")
