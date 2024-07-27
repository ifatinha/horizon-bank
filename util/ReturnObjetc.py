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
from classes.Deposit import Deposit
from classes.Withdraw import Withdraw
from classes.Transfer import Transfer

from datetime import datetime


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

    branch_address = Address.get_instance()
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
    address = Address.get_instance()

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
    address = Address.get_instance()

    company = Company(fullname, email, password, phone, address, ein, legal_name)

    return company


def find_branch_bd():
    branch_number = int(input("Agéncia: "))
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
    token = input("Token do Cliente: ")
    result = DatabaseOperations.find_customer_token(token)

    while result is None:
        print("@@@ Nenhum Cliente Encontrado. @@@")
        token = input("Token: ")
        result = DatabaseOperations.find_customer_token(token)

    id_customer, fullname, token = result
    customer = Customer(fullname, None, None, None, None)
    customer.customer_id = id_customer
    customer.token = token
    return customer


def return_account():
    print("### Conta Empresárial ###")
    customer = find_customer_bd()
    password = input("Senha: ")
    branch = find_branch_bd()

    account = Account(password, branch, customer)
    return account


def return_savign_account():
    print("### Conta Poupança ###")
    customer = find_customer_bd()
    password = input("Senha: ")
    branch = find_branch_bd()

    savign = SavignAccount(password, branch, customer)
    return savign


def return_current_account():
    print("### Conta Corrente ###")
    customer = find_customer_bd()
    password = input("Senha: ")
    branch = find_branch_bd()

    return CurrentAccount(password, branch, customer)


def return_historic(account):
    historic = Historic(account)

    return historic


def return_transaction_Deposit(historic_id, value):
    deposit = Deposit(value)
    return deposit.to_tuple() + (historic_id,)


def return_transaction_Withdraw(historic_id, value):
    withdraw = Withdraw(value)
    return withdraw.to_tuple() + (historic_id,)


def return_transaction_transfer(historic_id, value):
    transfer = Transfer(value)
    return transfer.to_tuple() + (historic_id,)
