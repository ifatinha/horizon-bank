from database.DatabaseOperations import DatabaseOperations
from connection.Connection import Connection

# DatabaseOperations.create_table(table_address_query)
conn = Connection()
conn.connect()
conn.check_and_create_database("solaris")
conn.close()
