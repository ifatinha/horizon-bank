from database.DatabaseOperations import DatabaseOperations
from classes.Address import Address
from classes.Manager import Manager
from classes.Branch import Branch
from classes.Individual import Individual
from classes.Company import Company
from classes.Account import Account
from classes.Customer import Customer
from classes.CurrentAccount import CurrentAccount
from classes.SavignAccount import SavignAccount
from classes.Historic import Historic

from datetime import datetime


def return_address():
    print("### Informações de Endereço ###")
    street = input("Endereço: ")
    number = input("Número: ")
    neighborhood = input("Bairro: ")
    postal_code = input("CEP: ")
    city = input("Cidade: ")
    state = input("Estado: ")

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
        address_type,
        notes,
    )


def return_manager():
    print("### Dados Pessoais ###")
    fullname = input("Nome Completo: ")
    email = input("Email: ")
    password = input("Senha: ")
    phone = input("Phone: ")
    employee_number = input("Número de Registro: ")

    is_exist = DatabaseOperations.find_manager_employee_number(employee_number)

    while is_exist is not None:
        print("@@@ Já existe um gerente com esse número. @@@")
        employee_number = input("Número de Registro: ")
        is_exist = DatabaseOperations.find_manager_employee_number(employee_number)

    address = return_address()

    manager = Manager(fullname, email, password, phone, address, employee_number)
    return manager


def find_manager_bd():
    print("### Gerente ###")
    manager_id = int(input("Digite o codigo do gerente: "))
    result = DatabaseOperations.find_manager_id(manager_id)

    while result is None:
        print("@@@ Nenhum Gerente Encontrado. @@@")
        manager_id = int(input("Codigo do gerente: "))
        result = DatabaseOperations.find_manager_id(manager_id)

    manager_id, fullname, email, password, phone, employee_number, manager_status = (
        result
    )

    manager = Manager(
        fullname, email, password, phone, None, employee_number, status=manager_status
    )
    manager.customer_id = manager_id

    return manager


def return_branch():

    print("### Informe os dados abaixo para cadastrar uma nova filial ###")
    branch_number = int(input("Número: "))
    branch_phone = input("Telefone: ")

    branch_address = return_address()
    manager = find_manager_bd()
    print(manager)

    branch = Branch(branch_number, branch_phone, branch_address, manager)

    return branch


def return_individual():
    print("### Dados Pessoais ###")
    fullname = input("Nome Completo: ")
    email = input("Email: ")
    password = input("Senha: ")
    phone = input("Telefone: ")
    ssn = input("SSN: ")
    birth = input("Data de Nascimento (dd/mm/yyyy): ")
    address = return_address()

    birth = datetime.strptime(birth, "%d/%m/%Y")
    individual = Individual(fullname, email, password, phone, address, ssn, birth)

    return individual


def return_company():
    print("### Dados da Empresa ###")
    fullname = input("Razão Social: ")
    email = input("Email: ")
    password = input("Senha: ")
    phone = input("Telefone: ")
    ein = input("EIN: ")
    legal_name = input("Nome Fantasia: ")
    address = return_address()

    company = Company(fullname, email, password, phone, address, ein, legal_name)

    return company


def find_branch_bd():
    branch_number = int(input("Código da Agéncia: "))
    result = DatabaseOperations.find_branch(branch_number)

    while result is None:
        print("@@@ Nenhuma Agência Encontrada. @@@")
        branch_number = int(input("Código da Agéncia: "))
        result = DatabaseOperations.find_branch(branch_number)

    id_branch, number, name = result
    branch = Branch(number, name, None, None, None)
    branch.id_branch = id_branch
    return branch


def find_customer_bd():
    customer_id = int(input("Codigo do Cliente: "))
    result = DatabaseOperations.find_customer(customer_id)

    while result is None:
        print("@@@ Nenhum Cliente Encontrado. @@@")
        customer_id = int(input("Codigo do Cliente: "))
        result = DatabaseOperations.find_customer(customer_id)

    id_customer, fullname = result
    customer = Customer(fullname, None, None, None, None)
    customer.customer_id = id_customer
    return customer


def return_account():
    print("### Conta Empresárial ###")
    password = input("Senha: ")

    branch = find_branch_bd()
    customer = find_customer_bd()
    account = Account(password, branch, customer)
    return account


def return_savign_account():
    print("### Conta Poupança ###")
    password = input("Senha: ")

    branch = find_branch_bd()
    customer = find_customer_bd()
    savign = SavignAccount(password, branch, customer)
    return savign


def return_current_account():
    print("### Conta Poupança ###")
    password = input("Senha: ")

    branch = find_branch_bd()
    customer = find_customer_bd()
    return CurrentAccount(password, branch, customer)


def return_historic(account):
    historic = Historic(account)

    return historic
