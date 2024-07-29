from classes.Historic import Historic


class HistoricCreator:

    @staticmethod
    def get_instance(account):
        return Historic(account)

    @staticmethod
    def from_db_record(record):
        return record[0]
