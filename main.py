from database.DatabaseOperations import DatabaseOperations
from sql.script_create_tables import create_database, create_tables, insert_default_user

from util.menu import (
    main_menu,
    manager_menu,
    client_menu,
    menu_type_customer,
    menu_type_account,
    menu_create_manager,
    menu_create_branch,
    menu_typle_customers,
    menu_banking_operations,
)

from util.ReturnObjetc import (
    return_manager,
    return_branch,
    return_individual,
    return_company,
    return_account,
    return_savign_account,
    return_current_account,
    return_historic,
    return_transaction_Deposit,
    return_transaction_Withdraw,
)


def main():

    # create_database()
    # create_tables()
    # insert_default_user()
    # SET SQL_SAFE_UPDATES=0;

    # f8d76506 4545

    # 5d98a027 1212
    # 5346144456 1515
    # 1028379526 1010
    # 6781090948 1111

    while True:

        option = main_menu()

        if option == "1":
            token = input("Token: ")
            password = input("Senha: ")

            status = DatabaseOperations.login_user(token, password)

            if len(status):
                cl_option = client_menu()

                if cl_option == "1":

                    """Operações Bancárias"""
                    number = input("Conta: ")
                    password = input("Senha: ")
                    account = DatabaseOperations.find_account_customer(number, password)

                    while account is None:
                        print("@@@ Nenhum conta encontrada. @@@")
                        number = input("Conta: ")
                        password = input("Senha: ")
                        account = DatabaseOperations.find_account_customer(
                            number, password
                        )

                    account_number, account_balance, account_type = account

                    while True:
                        option = menu_banking_operations()

                        if option == "1":
                            """Depósito"""
                            historic = DatabaseOperations.find_account_historic(
                                account_number
                            )
                            id_historic, id_account = historic

                            value = float(input("Valor do deposito: "))
                            DatabaseOperations.insert_deposit(
                                account_number, value, account_balance
                            )

                            transaction = return_transaction_Deposit(id_historic, value)
                            DatabaseOperations.insert_transaction(transaction)

                            account = DatabaseOperations.find_account_customer(
                                account_number, password
                            )

                            account_number, account_balance, account_type = account

                        elif option == "2":
                            """Saque"""
                            historic = DatabaseOperations.find_account_historic(
                                account_number
                            )
                            id_historic, id_account = historic

                            value = float(input("Valor do Saque: "))

                            DatabaseOperations.insert_withdraw(
                                account_number, value, account_balance
                            )

                            transaction = return_transaction_Withdraw(
                                id_historic, value
                            )
                            DatabaseOperations.insert_transaction(transaction)

                            account = DatabaseOperations.find_account_customer(
                                account_number, password
                            )
                            account_number, account_balance, account_type = account

                            pass
                        elif option == "3":
                            """Transferência"""
                            pass
                        elif option == "4":
                            """Extrato"""
                            print(f"Conta {account_number}")
                            historic_account = DatabaseOperations.list_historic(
                                account_number
                            )

                            if len(historic_account) > 0:
                                print("######### EXTRATO #########")
                                for historic in historic_account:
                                    print(historic)
                            else:
                                print("@@@ A conta não possui movimentações @@@")
                        elif option == "0":
                            break
                        else:
                            print("@@@ Opção Inválida. @@@")

                elif cl_option == "2":
                    """Minhas Contas"""
                    result = DatabaseOperations.find_accounts_individual(token)

                    if len(result) > 0:
                        print(result)
                    else:
                        print("@@@ Você não possui contas na agência. @@@")

                elif cl_option == "0":
                    break

                else:
                    print("\n@@@ Operação inválida, selecione novamente. @@@\n")

            else:
                print("@@@ Usuário ou senha inválidos @@@")

        elif option == "2":
            user = input("Token: ")
            password = input("Senha: ")

            status = DatabaseOperations.login_user(user=user, password=password)

            if len(status):

                mg_option = manager_menu()

                if mg_option == "1":
                    """Cadastrar Novo Cliente"""

                    while True:
                        tp_option = menu_type_customer()

                        if tp_option == "1":
                            """Pessoa Fisica"""
                            individual = return_individual()
                            id_customer = DatabaseOperations.insert_customer(
                                individual.customer_to_tuple()
                            )
                            id_address = DatabaseOperations.insert_address(
                                individual.address
                            )
                            DatabaseOperations.insert_address_customer(
                                id_address, id_customer
                            )
                            DatabaseOperations.insert_user(
                                individual.token, individual.password
                            )
                            DatabaseOperations.insert_invidual(
                                ((id_customer,) + individual.to_tuple())
                            )
                        elif tp_option == "2":
                            """Pessoa Juridica"""
                            company = return_company()
                            id_customer = DatabaseOperations.insert_customer(
                                company.customer_to_tuple()
                            )
                            id_address = DatabaseOperations.insert_address(
                                company.address
                            )
                            DatabaseOperations.insert_address_customer(
                                id_address, id_customer
                            )
                            DatabaseOperations.insert_user(
                                company.token, company.password
                            )

                            DatabaseOperations.insert_company(
                                ((id_customer,) + company.to_tuple())
                            )
                        elif tp_option == "0":
                            break

                        else:
                            print("@@@ Opção inválida @@@")

                elif mg_option == "2":
                    """Cadastrar Nova Conta"""

                    while True:
                        menu_option = menu_type_account()

                        if menu_option == "1":
                            """Conta Poupança"""
                            savign_account = return_savign_account()
                            id_account = DatabaseOperations.insert_account(
                                savign_account.super_to_tuple()
                            )

                            savign_account.id_account = id_account
                            DatabaseOperations.insert_savign_account(
                                savign_account.to_tuple()
                            )

                            historic = return_historic(savign_account)
                            DatabaseOperations.insert_historic(historic)

                        elif menu_option == "2":
                            """Conta Corrente"""
                            current_account = return_current_account()
                            id_account = DatabaseOperations.insert_account(
                                current_account.super_to_tuple()
                            )
                            current_account.id_account = id_account

                            DatabaseOperations.insert_current_account(
                                current_account.to_tuple()
                            )
                            historic = return_historic(current_account)
                            DatabaseOperations.insert_historic(historic)
                        elif menu_option == "3":
                            """Conta Empresárial"""

                            account = return_account()
                            id_account = DatabaseOperations.insert_account(
                                account.to_tuple()
                            )
                            account.id_account = id_account
                            historic = return_historic(account)
                            DatabaseOperations.insert_historic(historic)
                        elif menu_option == "0":
                            break

                        else:
                            print("@@@ Opção Inválida! Tente novamente. @@@")

                elif mg_option == "3":
                    """Contas Cliente"""

                    while True:
                        option = menu_type_customer()

                        if option == "1":
                            token = input("Token: ")
                            result = DatabaseOperations.find_accounts_individual(token)

                            if len(result) > 0:
                                print(result)
                            else:
                                print(
                                    "@@@ O cliente não encontrado ou não possui contas na agência. @@@"
                                )

                        elif option == "2":
                            token = input("Token: ")

                            result = DatabaseOperations.find_accounts_company(token)

                            if len(result) > 0:
                                print(result)
                            else:
                                print(
                                    "@@@ O cliente não encontrado ou não possui contas na agência. @@@"
                                )

                        elif option == "0":
                            print("@@@ Retornando ao menu principal. @@@")
                            break

                        else:
                            print("@@@ Opção Inválida! @@@")

                elif mg_option == "4":
                    """Listar Clientes"""

                    while True:
                        option = menu_typle_customers()

                        if option == "1":

                            result = DatabaseOperations.list_individual_customers()

                            if len(result):
                                print("##### CLIENTES ENCONTRADOS #####")
                                for client in result:
                                    print(client)
                            else:
                                print("@@@ Nenhum cliente encontrado. @@@")

                        elif option == "2":
                            print("##### CLIENTES ENCONTRADOS #####")
                            result = DatabaseOperations.list_company_customers()

                            if len(result):
                                for client in result:
                                    print(client)
                            else:
                                print("@@@ Nenhum cliente encontrado. @@@")

                        elif option == "0":
                            print("### Retornando ao menu principal. ###")
                            break
                        else:
                            print("@@@ Opção Inválida. @@@")

                elif mg_option == "5":
                    """Cadastrar Gerente"""

                    while True:
                        op_manager = menu_create_manager()

                        if op_manager == "1":
                            print(
                                "Informe os dados abaixo para cadastar um novo gerente"
                            )
                            manager = return_manager()
                            id_customer = DatabaseOperations.insert_customer(
                                manager.customer_to_tuple()
                            )
                            id_address = DatabaseOperations.insert_address(
                                manager.address
                            )
                            DatabaseOperations.insert_address_customer(
                                id_address, id_customer
                            )
                            DatabaseOperations.insert_user(
                                manager.token, manager.password
                            )
                            DatabaseOperations.insert_manager(
                                (id_customer,) + manager.to_tuple()
                            )

                        elif op_manager == "0":
                            break

                        else:
                            print("@@@ Opção Inválida! Tente novamente. @@@")

                elif mg_option == "6":
                    """Listar Gerentes"""
                    managers = DatabaseOperations.list_managers()

                    if len(managers) > 0:
                        for manager in managers:
                            print(manager)
                    else:
                        print("@@@ Nenhum gerente encontrado. @@@")

                elif mg_option == "7":
                    """Cadastrar Filial"""

                    while True:
                        op_branch = menu_create_branch()

                        if op_branch == "1":
                            branch = return_branch()
                            id_address = DatabaseOperations.insert_address(
                                branch.address
                            )
                            DatabaseOperations.insert_branch(
                                branch.to_tuple() + (id_address,)
                            )

                            DatabaseOperations.update_status_manager(
                                branch.manager.customer_id
                            )
                        elif op_branch == "0":
                            break
                        else:
                            print("@@@ Opção Inválida! Tente novamente. @@@")

                elif mg_option == "8":
                    """Agências Cadastradas"""
                    branchs = DatabaseOperations.list_branchs()

                    if len(branchs) > 0:
                        for branch in branchs:
                            print(branch)
                    else:
                        print("@@@ Nenhum gerente encontrado. @@@")

                elif mg_option == "0":
                    break

                else:
                    print("\n@@@ Operação inválida, selecione novamente. @@@\n")
            else:
                print("@@@ Usuário ou senha inválidos @@@")

        elif option == "0":
            break
        else:
            print("\n@@@ Operação inválida, selecione novamente. @@@\n")


main()
