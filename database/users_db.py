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
def insert_user(token, password):
    query = f"INSERT INTO users (token, password) VALUES(%s, %s)"
    try:
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (token, password))
        conn.commit()
        logging.info("Usuário inserido no banco de dados!")
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")


@staticmethod
def login_user(token, password):
    query = f"SELECT * FROM users WHERE token = %s AND password = %s"
    try:
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (token, password))
        resultado = cursor.fetchall()
        return resultado
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")
