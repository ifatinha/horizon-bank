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


def insert_historic(historic) -> None:
    """
    Insere um histórico das contas no banco de dados.

    Args:
        historic (Historic): Um objeto da classe Historic contendo os dados a serem inseridos.

    Returns:
        None
    """

    try:

        query = "INSERT INTO historic(id_account) VALUES(%s)"
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, historic.to_tuple())
        conn.commit()
        logging.info("Historico da conta criando.")

    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")
