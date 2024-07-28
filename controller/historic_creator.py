from classes.Historic import Historic


class HistoricCreator:

    @staticmethod
    def get_instance(account):
        return Historic(account)

    @staticmethod
    def from_db_record(record):
        historic = Historic(record[1])
        historic.id = record[0]

        return historic
