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

    employee_number = input("Número de Registro: ")
    is_exist = DatabaseOperations.find_manager_employee_number(employee_number)

    while is_exist is not None:
        print("@@@ Já existe um gerente com esse número. @@@")
        employee_number = input("Número de Registro: ")
        is_exist = DatabaseOperations.find_manager_employee_number(employee_number)

    fullname = input("Nome Completo: ")
    password = input("Senha: ")
    phone = input("Phone: ")

    address = return_address()
    email = Manager.generate_email(fullname)
    manager = Manager(fullname, email, password, phone, address, employee_number)
    return manager


def find_manager_bd():
    print("### Gerente ###")
    employee_number = int(input("Número do gerente: "))
    result = DatabaseOperations.find_manager_status(employee_number)

    while result is None:
        print("@@@ Nenhum Gerente Encontrado. @@@")
        employee_number = int(input("Codigo do gerente: "))
        result = DatabaseOperations.find_manager_status(employee_number)

    manager_id, fullname, employee_number, manager_status = result

    manager = Manager(
        fullname, None, None, None, None, employee_number, status=manager_status
    )
    manager.customer_id = manager_id

    return manager


def return_branch():

    print("### Informe os dados abaixo para cadastrar uma nova filial ###")
    branch_number = int(input("Número: "))
    result = DatabaseOperations.find_branch(branch_number)

    while result is not None:
        print("@@@ Já existe uma agência cadastrada com esse número. @@@")
        branch_number = int(input("Novo Número: "))
        result = DatabaseOperations.find_branch(branch_number)

    branch_address = return_address()
    manager = find_manager_bd()
    print(manager)

    branch = Branch(branch_number, branch_address, manager)

    return branch


def return_individual():
    print("### Dados Pessoais ###")
    ssn = input("SSN: ")
    result = DatabaseOperations.find_individual_ssn(ssn)

    while result is not None:
        print("@@@ Já existe uma pessoa cadastrada com esse ssn. @@@")
        ssn = input("SSN: ")
        result = DatabaseOperations.find_individual_ssn(ssn)

    fullname = input("Nome Completo: ")
    birth = input("Data de Nascimento (dd/mm/yyyy): ")
    birth = datetime.strptime(birth, "%d/%m/%Y")
    email = input("Email: ")
    password = input("Senha: ")
    phone = input("Telefone: ")
    address = return_address()

    individual = Individual(fullname, email, password, phone, address, ssn, birth)

    return individual


def return_company():
    print("### Dados da Empresa ###")
    ein = input("EIN: ")
    is_exist = DatabaseOperations.find_company_ein(ein)

    while is_exist is not None:
        print("@@@ Já existe uma empresa com o ein. @@@")
        ein = input("EIN: ")
        is_exist = DatabaseOperations.find_company_ein(ein)

    fullname = input("Razão Social: ")
    legal_name = input("Nome Fantasia: ")
    email = input("Email: ")
    password = input("Senha: ")
    phone = input("Telefone: ")
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

    branch_id, branch_number, branch_name = result
    branch = Branch(branch_number, None, None)
    branch.name = branch_name
    branch.id_branch = branch_id
    return branch


def find_customer_bd():
    token = int(input("Token: "))
    result = DatabaseOperations.find_customer(token)

    while result is None:
        print("@@@ Nenhum Cliente Encontrado. @@@")
        token = int(input("Token: "))
        result = DatabaseOperations.find_customer_token(token)

    id_customer, fullname, token = result
    customer = Customer(fullname, None, None, None, None)
    customer.customer_id = id_customer
    customer.token = token
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
    print("### Conta Corrente ###")
    password = input("Senha: ")

    branch = find_branch_bd()
    customer = find_customer_bd()
    return CurrentAccount(password, branch, customer)


def return_historic(account):
    historic = Historic(account)

    return historic
