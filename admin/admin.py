from util.menu import manager_menu, menu_manager_customers

from admin.admin_operations import AdminOperations


def admin_operations():

    while True:

        mg_option = manager_menu()

        if mg_option == "1":

            while True:

                option_customer = menu_manager_customers()

                if option_customer == "1":

                    AdminOperations.register_customers()

                elif option_customer == "2":

                    AdminOperations.open_accounts()

                elif option_customer == "3":

                    AdminOperations.list_customers()

                elif option_customer == "4":

                    AdminOperations.search_customer_data()

                elif option_customer == "0":
                    break
                else:
                    print("\n@@@ Operação inválida, selecione novamente. @@@\n")

        elif mg_option == "2":

            AdminOperations.manager_customers()

        elif mg_option == "3":

            AdminOperations.manager_branchs()

        elif mg_option == "0":
            break
        else:
            print("\n@@@ Operação inválida, selecione novamente. @@@\n")
