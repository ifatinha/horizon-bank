import mysql.connector
import mysql.connector.errorcode
import logging
from mysql.connector import Error
from pathlib import Path
from connection.config import user, password, host, database

# Configuração básica do logging para registrar em um arquivo
file_path = Path(__file__).resolve().parents[1] / "logs" / "mysql_logs.log"

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class Connection:

    def __init__(self):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        """Cria e retorna uma conexão com o servidor MySQL."""
        try:
            self.connection = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=self.database,
            )

            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                logging.info("Conexão bem-sucedida!")
                return self.connection

        except mysql.connector.Error as err:
            logging.error(f"Erro ao conectar: {err}")
            return None

    def close(self):
        """Fecha a conexão com o servidor MySQL."""
        if self.connection is not None and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            logging.info("Conexão fechada.")
        else:
            logging.info("A conexão já estava fechada ou não foi estabelecida.")

    @staticmethod
    def check_and_create_database(db_name):
        """Verifica se um banco de dados existe e, se não, cria-o."""
        conn = mysql.connector.connect(user=user, password=password, host=host)
        cursor = conn.cursor()

        try:

            cursor.execute(f"SHOW DATABASES LIKE '{db_name}';")
            result = cursor.fetchone()

            if result:
                logging.info(f"O bando de dados `'{db_name}'` já existe.")
                logging.info(f"Estabelecendo conexão.")
            else:
                logging.info(f"O banco de dados `'{db_name}'` não existe.")
                logging.info("Criando banco de dados.")
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")
                logging.info(f"Banco de dados `'{db_name}'` criado com sucesso!")
        except Error as err:
            if err.errno == mysql.connector.errorcode.ER_DB_CREATE_EXISTS:
                logging.error(f"Erro ao verificar/criar banco de dados: {err}.")
            else:
                logging.error(f"Erro ao criar o banco de dados: {err}")
        finally:
            if cursor is not None:
                cursor.close()
                logging.info(f"Cursor fechado.")
