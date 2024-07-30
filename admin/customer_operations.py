from util.menu import client_menu
from util.menu import menu_banking_operations
from database.account_db import list_accounts_customer, find_balance_account
from controller.account_creator import AccountCreator
from admin.banking_operations import BankingOperations


def customer_operations(token):

    while True:

        client_option = client_menu()

        if client_option == "1":

            # Operações bancárias

            account = AccountCreator.from_db_record(BankingOperations.find_account())
            historic = BankingOperations.return_historic_account(account.number)
            print(account)

            while True:

                banking_operations = menu_banking_operations()
                account_balance = find_balance_account(account.number)

                if banking_operations == "1":
                    # Deposito
                    BankingOperations.deposit(
                        account.number, account.balance, historic[0]
                    )
                elif banking_operations == "2":
                    # Saque
                    BankingOperations.withdrawal(
                        account.number, account.balance, historic[0]
                    )
                elif banking_operations == "3":
                    # Transferência
                    BankingOperations.transfer(
                        account.number, account.balance, historic[0]
                    )

                elif banking_operations == "4":

                    BankingOperations.transactions_account(account.number)
                    print(f"Saldo: R$ {float(account_balance[0]):.2f}\n")

                elif banking_operations == "0":
                    break
                else:
                    print("@@@ Operação inválida. Tente novamente. @@@")

        elif client_option == "2":
            # Contas Cadastradas

            accounts_customer = list_accounts_customer(token)

            if accounts_customer:

                print("CONTAS ENCONTRADAS")

                for account in accounts_customer:
                    print("=" * 60)
                    print(AccountCreator.from_db_record(account))
                    print("=" * 60 + "\n")

            else:
                print("@@@ Você não possui contas. @@@")

        elif client_option == "0":
            break

        else:
            print("\n@@@ Operação inválida, selecione novamente. @@@\n")
