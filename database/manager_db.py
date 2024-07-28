from connection.Connection import Connection
from database.customer_db import insert_customer
from database.address_db import insert_address, insert_address_customer
from database.users_db import insert_user
from mysql.connector import Error
from pathlib import Path
import logging


file_path = Path(__file__).resolve().parents[1] / "logs" / "mysql_logs.log"

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def insert_manager(manager):

    try:

        conn = Connection().connect()
        cursor = conn.cursor()

        # Inserindo os dados do customer na tabela customer
        id_customer = insert_customer(manager.customer_to_tuple())

        # Inserindo os dados do endereço
        id_address = insert_address(manager.address)

        # Inserindo os dados de referencia de customer e endereço
        insert_address_customer(id_address, id_customer)

        # Inserindo os dados de acesso
        insert_user(manager.token, manager.password)

        query = """INSERT INTO manager(manager_id, employee_number, hire_date, manager_status)
                VALUES(%s, %s, %s, %s)"""
        cursor.execute(query, (id_customer,) + manager.to_tuple())

        conn.commit()
        print("### Gerente cadastrado com sucesso. ###")
        logging.info("Gerente inserido no banco de dados.")

    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")


def list_managers():
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
            M.employee_number, 
            M.hire_date, 
            M.manager_status
            FROM customer C
            INNER JOIN 
                manager M ON C.id = M.manager_id
            INNER JOIN 
                address_customer AC ON AC.id_customer = M.manager_id
            INNER JOIN 
                address A ON A.id = AC.id_address;
            """

    try:
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")


def find_manager_employee_number(employee_number):
    query = "SELECT employee_number FROM manager WHERE employee_number = %s"

    try:
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (employee_number,))
        resultado = cursor.fetchone()
        return resultado
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")


def find_manager_status(employee_number):
    query = """
        SELECT 
            C.id,
            C.fullname, 
            C.email, 
            C.phone, 
            M.employee_number, 
            M.hire_date, 
            M.manager_status, 
            A.number, 
            A.street, 
            A.postal_code, 
            A.neighborhood, 
            A.city, 
            A.state, 
            A.country, 
            A.address_type, 
            A.is_primary, 
            A.notes
            FROM customer C
            INNER JOIN 
                manager M ON C.id = M.manager_id
            INNER JOIN 
                address_customer AC ON AC.id_customer = M.manager_id
            INNER JOIN 
                address A ON A.id = AC.id_address
			WHERE M.employee_number = %s AND M.manager_status = TRUE;
    """
    try:
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (employee_number,))
        resultado = cursor.fetchone()
        return resultado
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")


def update_status_manager(employee_number):
    query = "UPDATE manager SET manager_status = False where employee_number = %s"

    try:
        conn = Connection().connect()
        cursor = conn.cursor()
        cursor.execute(query, (employee_number,))
        conn.commit()
    except Error as err:
        logging.error(f"Erro ao executar SQL: {err}")
    finally:
        if conn:
            conn.close()
            logging.info("Conexão fechada!")
