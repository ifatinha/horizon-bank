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
        """Cria e retorna uma conexão com o servidor MySQL."""
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
                return self.connection

        except mysql.connector.Error as err:
            print(f"Erro ao conectar: {err}")
            return None

    def close(self):
        """Fecha a conexão com o servidor MySQL."""
        if self.connection is not None and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Conexão fechada.")
        else:
            print("A conexão já estava fechada ou não foi estabelecida.")

    @staticmethod
    def check_and_create_database(db_name):
        """Verifica se um banco de dados existe e, se não, cria-o."""
        conn = mysql.connector.connect(user=user, password=password, host=host)
        cursor = conn.cursor()
        try:

            cursor.execute(f"SHOW DATABASES LIKE '{db_name}';")
            result = cursor.fetchone()

            if result:
                print(f"O bando de dados `'{db_name}'` já existe.")
                print(f"Estabelecendo conexão.")
            else:
                print(f"O banco de dados `'{db_name}'` não existe.")
                print("Criando banco de dados.")
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")
                print(f"Banco de dados `'{db_name}'` criado com sucesso!")
        except Error as err:
            if err.errno == mysql.connector.errorcode.ER_DB_CREATE_EXISTS:
                print(f"Erro ao verificar/criar banco de dados: {err}.")
            else:
                print(f"Erro ao criar o banco de dados: {err}")
        finally:
            if cursor is not None:
                cursor.close()
                print(f"Cursor fechado.")
