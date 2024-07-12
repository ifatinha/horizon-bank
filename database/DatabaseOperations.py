from connection.Connection import Connection


class DatabaseOperations:

    @staticmethod
    def connect():
        return Connection()
