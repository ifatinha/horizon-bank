from database.create_db import CreateDatabase
from util.menu import main_menu
from database.users_db import login_user
from admin.admin import admin_operations
from admin.customer_operations import customer_operations


def main():

    # CreateDatabase()
    # SET SQL_SAFE_UPDATES=0;

    # banco de casa
    # e2828d07 5656
    # 7643713067 1515

    # transfert account
    # f8d76506 4545
    # 6620287101 1515

    # Banco do posto
    # 5d98a027 1212
    # 6781090948 1111

    # cdd923f5 4545
    # 9470389487 1515

    while True:

        option = main_menu()

        if option == "1":

            token = input("Token: ")
            password = input("Senha: ")

            status = login_user(token, password)

            if status:
                customer_operations(token)
            else:
                print("@@@ Usuário ou senha inválidos @@@")

        elif option == "2":

            token = input("Token: ")
            password = input("Senha: ")

            status = login_user(token=token, password=password)

            if status:
                admin_operations()
            else:
                print("@@@ Usuário ou senha inválidos @@@")

        elif option == "0":
            break
        else:
            print("\n@@@ Operação inválida, selecione novamente. @@@\n")


if __name__ == "__main__":
    main()
