from database.DatabaseOperations import DatabaseOperations
from classes.Address import Address
from classes.Manager import Manager
from classes.Branch import Branch


def return_address():
    print("### Endereço ###")
    street = input("Rua: ")
    number = input("Número: ")
    neighborhood = input("Bairro: ")
    postal_code = input("CEP: ")
    city = input("Cidade: ")
    state = input("Estado: ")
    country = input("Pais: ")

    while True:
        type_address = int(
            input(
                "Tipo de Endereço: ('[1] - Residential', '[2] - Business', '[3] - Shipping', '[4] - Billing'): "
            )
        )

        if type_address == 1:
            address_type = "Residential"
            break
        elif type_address == 2:
            address_type = "Business"
            break
        elif type_address == 3:
            address_type = "Shipping"
            break
        elif type_address == 4:
            address_type = "Billing"
            break
        else:
            print("@@@ Opção Inválida, tente novamente.")

    notes = input("Detalhes: ")

    return Address(
        number,
        street,
        postal_code,
        neighborhood,
        city,
        state,
        country,
        address_type,
        notes,
    )


def return_manager():
    print("### Dados Pessoais ###")
    fullname = input("Nome Completo: ")
    email = input("Email: ")
    phone = input("Phone: ")
    employee_number = input("Número de Registro: ")
    address = return_address()

    manager = Manager(fullname, email, phone, address, employee_number)
    return manager


def find_manager_bd():
    print("### Gerente ###")
    manager_id = int(input("Digite o codigo do gerente: "))
    result = DatabaseOperations.find_manager(manager_id)

    while result is None:
        print("@@@ Nenhum Gerente Encontrado. @@@")
        manager_id = int(input("Codigo do gerente: "))
        result = DatabaseOperations.find_manager(manager_id)

    manager_id, fullname, email, phone, employee_number, manager_status = result

    manager = Manager(
        fullname, email, phone, None, employee_number, status=manager_status
    )
    manager.customer_id = manager_id

    return manager


def return_branch():

    print("### Informe os dados abaixo para cadastrar uma nova filial ###")
    branch_number = int(input("Número: "))
    branch_name = input("Nome: ")

    branch_address = return_address()
    manager = find_manager_bd()

    branch = Branch(branch_number, branch_name, branch_address, manager)
    return branch
