from connection.Connection import Connection
from mysql.connector import Error
from pathlib import Path
import mysql.connector
import mysql.connector.errorcode
import logging

# Configuração básica do logging para registrar em um arquivo
file_path = Path(__file__).resolve().parents[1] / "logs" / "mysql_logs.log"

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class DatabaseOperations:

    @staticmethod
    def getConnect():
        conn = Connection()
        return conn

    @staticmethod
    def create_table(table_creation_query):
        try:
            conn = DatabaseOperations.getConnect()
            conn.connect()
            conn.cursor.execute(table_creation_query)
            logging.info("Tabela Criada!")
        except Error as err:
            logging.error(f"Erro ao criar a tabela: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def login_admin(user, passowrd):
        query = f"SELECT * FROM admin WHERE user = %s AND password = %s"
        try:
            conn = DatabaseOperations.getConnect()
            conn.connect()
            conn.cursor.execute(query, (user, passowrd))
            resultado = conn.cursor.fetchall()
            return resultado
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    def insert_address(address):
        query = "INSERT INTO address(number, street, postal_code, neighborhood, city, state, country, address_type, is_primary, notes) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            conn = DatabaseOperations.getConnect().connect()
            cursor = conn.cursor()
            cursor.execute(query, address.to_tuple())
            conn.commit()
            return cursor.lastrowid
        except Error as err:
            logging.error(f"Erro ao executar SQL: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")
