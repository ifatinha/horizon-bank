from database.DatabaseOperations import DatabaseOperations
from connection.Connection import Connection

# Connection.check_and_create_database("horizon_Bank")

conn = Connection()
conn.connect()
conn.close()
