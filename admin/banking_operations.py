from database.account_db import find_account, find_account_number
from database.historic_db import find_historic
from database.transaction_db import (
    list_transactions_account,
    insert_deposit,
    insert_transaction,
    insert_withdraw,
)
from controller.transaction_creator import TransactionCreator
from controller.account_creator import AccountCreator
from classes.Withdraw import Withdraw
from classes.Deposit import Deposit
from classes.Transfer import Transfer


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
            return False

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
            return True
        else:
            print("@@@ Falha ao efetuar o saque. Tente novamente. @@@")
            return False

    @staticmethod
    def transfer(account_from_number, account_from_balance, historic_id):
        """
        Realiza a transferência de um valor entre contas bancárias.

        Parâmetros:
        account_from_number (str): Número da conta de origem.
        account_from_balance (float): Saldo atual da conta de origem.
        historic_id (int): ID histórico da transação.

        Retorna:
        bool: True se a transferência for bem-sucedida, False caso contrário.
        """

        account_to = AccountCreator.from_db_record(
            BankingOperations.find_account_transfer()
        )

        historic_account_to = BankingOperations.return_historic_account(
            account_to.number
        )

        value = BankingOperations.get_transfer_value()

        # Realiza o saque na conta de origem
        if insert_withdraw(account_from_number, value, account_from_balance):
            # Realiza o depósito na conta de destino
            if insert_deposit(account_to.number, value, account_to.balance):
                # Registra a transação para a conta de origem
                transaction_from = Transfer(value)
                insert_transaction(transaction_from.to_tuple(historic_id))

                # Registra a transação para a conta de destino
                transaction_to = Transfer(value)
                insert_transaction(transaction_to.to_tuple(historic_account_to[0]))

                print(
                    f"==== Transferência de R$ {value:.2f} efetuada com sucesso. ===="
                )
                return True
            else:
                print("@@@ Falha no depósito da conta de destino. @@@")
                return False
        else:
            print("@@@ Falha no saque da conta de origem. @@@")
            return False

    @staticmethod
    def get_transfer_value():
        while True:
            try:
                value = float(input("Valor a transferir: "))
                break
            except ValueError:
                print("Por favor, insira um valor numérico válido.")
        return value

    @staticmethod
    def find_account_transfer():

        while True:

            try:
                account_to_number = int(input("Transferir para: "))
            except ValueError:
                print("Por favor, insira um valor numérico válido.")
                continue

            account = find_account_number(account_to_number)

            if account:
                return account
            else:
                print("@@@ Nenhuma conta encontra. Tente novamente. @@@")
