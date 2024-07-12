from connection.Connection import Connection
from mysql.connector import Error
import mysql.connector
import mysql.connector.errorcode


class DatabaseOperations:

    @staticmethod
    def getConnect():
        conn = Connection()
        return conn

    def create_table(table_creation_query):
        try:
            conn = DatabaseOperations.getConnect()
            conn.connect()
            conn.cursor.execute(table_creation_query)
        except Error as err:
            print(f"Erro ao criar a tabela: {err}")
        finally:
            if conn:
                conn.close()

    def insert(insert_query):
        try:
            conn = DatabaseOperations.getConnect()
            conn.connect()
            conn.cursor.execute(insert_query)
            conn.commit()
        except Error as err:
            print(f"Erro ao criar a tabela: {err}")
        finally:
            if conn:
                conn.close()
