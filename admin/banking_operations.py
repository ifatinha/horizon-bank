from database.account_db import find_account
from database.historic_db import find_historic
from database.transaction_db import (
    list_transactions_account,
    insert_deposit,
    insert_transaction,
    insert_withdraw,
)
from controller.transaction_creator import TransactionCreator
from classes.Withdraw import Withdraw
from classes.Deposit import Deposit


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
    def deposit(account_number, account_balance, historic_id):
        while True:
            try:
                value = float(input("Valor do depósito: "))
                break
            except ValueError:
                print("Por favor, insira um valor numérico válido.")

        status = insert_deposit(account_number, value, account_balance)

        if status:
            transaction = Deposit(value)
            insert_transaction(transaction.to_tuple(historic_id))
            print(f"==== Depósito de R$ {value:.2f} efetuado com sucesso. ====")
            return True
        else:
            print("@@@ Falha ao efetuar o depósito. Tente novamente. @@@")
            return True

    @staticmethod
    def withdrawal(account_number, account_balance, historic_id):
        while True:
            try:
                value = float(input("Valor do saque: "))
                break
            except ValueError:
                print("Por favor, insira um valor numérico válido.")

        status = insert_withdraw(account_number, value, account_balance)

        if status:
            transaction = Withdraw(value)
            insert_transaction(transaction.to_tuple(historic_id))
            print(f"==== Saque de R$ {value:.2f} efetuado com sucesso. ====")
        else:
            print("@@@ Falha ao efetuar o saque. Tente novamente. @@@")
