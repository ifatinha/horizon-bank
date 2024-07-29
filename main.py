from sql.script_create_tables import create_database, create_tables, insert_default_user

from util.menu import main_menu
from database.users_db import login_user
from admin.admin import admin_operations
from admin.customer_operations import customer_operations


def main():

    # create_database()
    # create_tables()
    # insert_default_user()
    # SET SQL_SAFE_UPDATES=0;

    # f8d76506 4545

    # e2828d07 5656
    # 7643713067 1515

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
