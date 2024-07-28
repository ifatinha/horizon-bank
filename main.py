from database.DatabaseOperations import DatabaseOperations
from sql.script_create_tables import create_database, create_tables, insert_default_user
from controller.manager_creator import ManagerCreator
from controller.branch_creator import BranchCreator

from util.menu import (
    main_menu,
    manager_menu,
    client_menu,
    menu_type_customer,
    menu_type_account,
    menu_managers,
    menu_branchs,
    menu_typle_customers,
    menu_banking_operations,
)

from util.ReturnObjetc import (
    return_individual,
    return_company,
    return_account,
    return_savign_account,
    return_current_account,
    return_historic,
    return_transaction_Deposit,
    return_transaction_Withdraw,
    return_transaction_transfer,
)

from database.users_db import insert_user, login_user
from database.manager_db import insert_manager, list_managers
from database.branch_db import insert_branch, list_branchs


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

            status = login_user(token, password)

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
                    historic = DatabaseOperations.find_account_historic(account_number)
                    id_historic, id_account = historic

                    while True:
                        option = menu_banking_operations()

                        if option == "1":
                            """Depósito"""
                            historic = DatabaseOperations.find_account_historic(
                                account_number
                            )
                            id_historic, id_account = historic

                            value = float(input("Valor do deposito: "))
                            result = DatabaseOperations.insert_deposit(
                                account_number, value, account_balance
                            )

                            if result:

                                transaction = return_transaction_Deposit(
                                    id_historic, value
                                )
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

                            result = DatabaseOperations.insert_withdraw(
                                account_number, value, account_balance
                            )

                            if result:

                                transaction = return_transaction_Withdraw(
                                    id_historic, value
                                )
                                DatabaseOperations.insert_transaction(transaction)

                            account = DatabaseOperations.find_account_customer(
                                account_number, password
                            )
                            account_number, account_balance, account_type = account

                        elif option == "3":
                            """Transferência"""

                            # Dados da conta de destino
                            numero_conta_transferencia = int(
                                input("Conta para transferência: ")
                            )

                            conta_transferencia = DatabaseOperations.find_account(
                                numero_conta_transferencia
                            )

                            while conta_transferencia is None:
                                print("@@@ Nenhum conta encontrada. @@@")
                                numero_conta_transferencia = int(
                                    input("Conta para transferência: ")
                                )

                                conta_transferencia = DatabaseOperations.find_account(
                                    numero_conta_transferencia
                                )

                            conta_transfer_number, conta_transfer_balance = (
                                conta_transferencia
                            )

                            conta_destino_historico = (
                                DatabaseOperations.find_account_historic(
                                    conta_transfer_number
                                )
                            )

                            id_historico_conta_destino, id_historico_conta_destino = (
                                conta_destino_historico
                            )

                            valor_transferencia = float(
                                input("Valor a ser transferido: ")
                            )

                            result_saque = DatabaseOperations.insert_withdraw(
                                account_number, valor_transferencia, account_balance
                            )

                            if result_saque:

                                transaction = return_transaction_transfer(
                                    id_historic, valor_transferencia
                                )
                                DatabaseOperations.insert_transaction(transaction)

                                account = DatabaseOperations.find_account_customer(
                                    account_number, password
                                )
                                account_number, account_balance, account_type = account

                                result_deposito = DatabaseOperations.insert_deposit(
                                    conta_transfer_number,
                                    valor_transferencia,
                                    conta_transfer_balance,
                                )

                                if result_deposito:
                                    transaction = return_transaction_transfer(
                                        id_historico_conta_destino, valor_transferencia
                                    )
                                    DatabaseOperations.insert_transaction(transaction)

                                    conta_transferencia = (
                                        DatabaseOperations.find_account(
                                            numero_conta_transferencia
                                        )
                                    )

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

            status = login_user(user=user, password=password)

            if len(status):

                while True:
                    mg_option = manager_menu()

                    if mg_option == "1":
                        """Gerenciar Clientes"""

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
                                insert_user(individual.token, individual.password)
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
                                insert_user(company.token, company.password)

                                DatabaseOperations.insert_company(
                                    ((id_customer,) + company.to_tuple())
                                )
                            elif tp_option == "0":
                                break

                            else:
                                print("@@@ Opção inválida @@@")

                    elif mg_option == "20":
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

                    elif mg_option == "30":
                        """Contas Cliente"""

                        while True:
                            option = menu_type_customer()

                            if option == "1":
                                token = input("Token: ")
                                result = DatabaseOperations.find_accounts_individual(
                                    token
                                )

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

                    elif mg_option == "40":
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

                    elif mg_option == "2":

                        """Gerenciamento de Gerentes"""

                        while True:
                            option_manager = menu_managers()

                            if option_manager == "1":

                                """Novo Gerente"""
                                manager = ManagerCreator.get_instance()
                                insert_manager(manager)

                            elif option_manager == "2":

                                """Gerentes Cadastrados"""
                                managers = list_managers()

                                if managers:
                                    for manager in managers:
                                        print("====================================")
                                        print(ManagerCreator.from_db_record(manager))
                                        print("====================================\n")

                                else:
                                    print("@@@ Nenhum gerente cadastrado. @@@")
                            elif option_manager == "0":
                                """Retornando ao menu principal"""
                                break
                            else:
                                print(
                                    "\n@@@ Operação inválida, selecione novamente. @@@\n"
                                )

                    elif mg_option == "3":
                        """Gerenciamento de Agências"""

                        while True:

                            option_branch = menu_branchs()

                            if option_branch == "1":
                                """Cadastrar nova agência"""
                                branch = BranchCreator.get_instance()
                                insert_branch(branch)
                            elif option_branch == "2":
                                """Agências Cadastradas"""

                                branchs = list_branchs()

                                if len(branchs) > 0:
                                    for branch in branchs:
                                        print("==================================")
                                        print(BranchCreator.from_db_record(branch))
                                        print("==================================\n")
                                else:
                                    print("@@@ Nenhum gerente encontrado. @@@")

                            elif option_branch == "0":
                                """Saindo do menu"""
                                break
                            else:
                                print(
                                    "\n@@@ Operação inválida, selecione novamente. @@@\n"
                                )

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


if __name__ == "__main__":
    main()
