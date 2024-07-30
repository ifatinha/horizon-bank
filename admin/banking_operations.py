from database.account_db import find_account
from database.historic_db import find_historic
from database.transaction_db import (
    list_transactions_account,
    insert_deposit,
    insert_transaction,
)
from controller.transaction_creator import TransactionCreator
from classes.Withdraw import Withdraw


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

    @staticmethod
    def transactions_account(account_number):
        transactions = list_transactions_account(account_number)

        if transactions:
            print("################ HISTORICO DE MOVIMENTAÇÕES ################")
            for transaction in transactions:
                print("=" * 60)
                print(TransactionCreator.from_db_record(transaction))
                print("=" * 60 + "\n")
        else:
            print("@@@ Conta não possui movimentações. @@@")

    @staticmethod
    def deposit(account_number, value, account_balance, historic_id):
        status = insert_deposit(account_number, value, account_balance)

        if status:
            transaction = Withdraw(value)
            insert_transaction
