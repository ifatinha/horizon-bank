import mysql.connector
import mysql.connector.errorcode
from mysql.connector import Error
from connection.config import user, password, host, database


class Connection:

    def __init__(self):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=self.database,
            )

            if self.connection.is_connected():
                print("Conexão bem-sucedida!")
                self.cursor = self.connection.cursor()

        except mysql.connector.Error as err:
            print(f"Erro ao conectar: {err}")

    def create_database(self, db_name):
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"Banco de dados {db_name} criado com sucesso!")
        except Error as err:
            if err.errno == mysql.connector.errorcode.ER_DB_CREATE_EXISTS:
                print(f"O banco de dados {db_name} já existe.")
            else:
                print(f"Erro ao criar o banco de dados: {err}")
        finally:
            if self.cursor:
                self.cursor.close()

    def create_table(self, table_creation_query):

        try:
            cursor = self.connection.cursor()
            cursor.execute(table_creation_query)
        except Error as err:
            print(f"Erro ao criar a tabela: {err}")
        finally:
            if cursor:
                cursor.close()

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexão fechada.")
