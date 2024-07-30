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
                    pass
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

    #     cl_option = client_menu()

    #     if cl_option == "1":

    #         """Operações Bancárias"""
    #         number = input("Conta: ")
    #         password = input("Senha: ")
    #         account = DatabaseOperations.find_account_customer(number, password)

    #         while account is None:
    #             print("@@@ Nenhum conta encontrada. @@@")
    #             number = input("Conta: ")
    #             password = input("Senha: ")
    #             account = DatabaseOperations.find_account_customer(
    #                 number, password
    #             )

    #         account_number, account_balance, account_type = account
    #         historic = DatabaseOperations.find_account_historic(account_number)
    #         id_historic, id_account = historic

    #         while True:
    #             option = menu_banking_operations()

    #             if option == "1":
    #                 """Depósito"""
    #                 historic = DatabaseOperations.find_account_historic(
    #                     account_number
    #                 )
    #                 id_historic, id_account = historic

    #                 value = float(input("Valor do deposito: "))
    #                 result = DatabaseOperations.insert_deposit(
    #                     account_number, value, account_balance
    #                 )

    #                 if result:

    #                     transaction = return_transaction_Deposit(
    #                         id_historic, value
    #                     )
    #                     DatabaseOperations.insert_transaction(transaction)

    #                 account = DatabaseOperations.find_account_customer(
    #                     account_number, password
    #                 )

    #                 account_number, account_balance, account_type = account

    #             elif option == "2":
    #                 """Saque"""
    #                 historic = DatabaseOperations.find_account_historic(
    #                     account_number
    #                 )
    #                 id_historic, id_account = historic

    #                 value = float(input("Valor do Saque: "))

    #                 result = DatabaseOperations.insert_withdraw(
    #                     account_number, value, account_balance
    #                 )

    #                 if result:

    #                     transaction = return_transaction_Withdraw(
    #                         id_historic, value
    #                     )
    #                     DatabaseOperations.insert_transaction(transaction)

    #                 account = DatabaseOperations.find_account_customer(
    #                     account_number, password
    #                 )
    #                 account_number, account_balance, account_type = account

    #             elif option == "3":
    #                 """Transferência"""

    #                 # Dados da conta de destino
    #                 numero_conta_transferencia = int(
    #                     input("Conta para transferência: ")
    #                 )

    #                 conta_transferencia = DatabaseOperations.find_account(
    #                     numero_conta_transferencia
    #                 )

    #                 while conta_transferencia is None:
    #                     print("@@@ Nenhum conta encontrada. @@@")
    #                     numero_conta_transferencia = int(
    #                         input("Conta para transferência: ")
    #                     )

    #                     conta_transferencia = DatabaseOperations.find_account(
    #                         numero_conta_transferencia
    #                     )

    #                 conta_transfer_number, conta_transfer_balance = (
    #                     conta_transferencia
    #                 )

    #                 conta_destino_historico = (
    #                     DatabaseOperations.find_account_historic(
    #                         conta_transfer_number
    #                     )
    #                 )

    #                 id_historico_conta_destino, id_historico_conta_destino = (
    #                     conta_destino_historico
    #                 )

    #                 valor_transferencia = float(
    #                     input("Valor a ser transferido: ")
    #                 )

    #                 result_saque = DatabaseOperations.insert_withdraw(
    #                     account_number, valor_transferencia, account_balance
    #                 )

    #                 if result_saque:

    #                     transaction = return_transaction_transfer(
    #                         id_historic, valor_transferencia
    #                     )
    #                     DatabaseOperations.insert_transaction(transaction)

    #                     account = DatabaseOperations.find_account_customer(
    #                         account_number, password
    #                     )
    #                     account_number, account_balance, account_type = account

    #                     result_deposito = DatabaseOperations.insert_deposit(
    #                         conta_transfer_number,
    #                         valor_transferencia,
    #                         conta_transfer_balance,
    #                     )

    #                     if result_deposito:
    #                         transaction = return_transaction_transfer(
    #                             id_historico_conta_destino, valor_transferencia
    #                         )
    #                         DatabaseOperations.insert_transaction(transaction)

    #                         conta_transferencia = (
    #                             DatabaseOperations.find_account(
    #                                 numero_conta_transferencia
    #                             )
    #                         )

    #             elif option == "4":
    #                 """Extrato"""
    #                 print(f"Conta {account_number}")
    #                 historic_account = DatabaseOperations.list_historic(
    #                     account_number
    #                 )

    #                 if len(historic_account) > 0:
    #                     print("######### EXTRATO #########")
    #                     for historic in historic_account:
    #                         print(historic)
    #                 else:
    #                     print("@@@ A conta não possui movimentações @@@")
    #             elif option == "0":
    #                 break
    #             else:
    #                 print("@@@ Opção Inválida. @@@")


#     elif cl_option == "2":
#         """Minhas Contas"""
#         result = DatabaseOperations.find_accounts_individual(token)

#         if len(result) > 0:
#             print(result)
#         else:
#             print("@@@ Você não possui contas na agência. @@@")

#     elif cl_option == "0":
#         break

#     else:
#         print("\n@@@ Operação inválida, selecione novamente. @@@\n")

# else:
#     print("@@@ Usuário ou senha inválidos @@@")
