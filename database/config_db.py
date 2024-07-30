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


class ConfigDatabase:

    @staticmethod
    def create_table(table_creation_query):
        try:
            conn = Connection().connect()
            conn.cursor.execute(table_creation_query)
            logging.info("Tabela Criada!")
        except Error as err:
            logging.error(f"Erro ao criar a tabela: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")

    @staticmethod
    def execute_sql_procedure(sql_procedure):
        try:
            conn = Connection().connect()
            conn.cursor.execute(sql_procedure)
            logging.info("Procedure Criada!")
        except Error as err:
            logging.error(f"Erro ao criar procedure: {err}")
        finally:
            if conn:
                conn.close()
                logging.info("Conexão fechada!")
