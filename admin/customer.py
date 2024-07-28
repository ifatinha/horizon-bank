def customer_operations():
    pass
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
