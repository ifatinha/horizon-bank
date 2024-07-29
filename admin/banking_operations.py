from database.account_db import find_account
from database.historic_db import find_historic
from controller.historic_creator import HistoricCreator


class BankingOperations:

    @staticmethod
    def find_account():

        while True:
            account_number = int(input("Conta: "))
            password = input("Senha: ")

            record = find_account(account_number, password)

            if record:
                return record

            print("@@@ Conta não encontrada. @@@")

    @staticmethod
    def return_historic_account(account_number):
        return find_historic(account_number)
