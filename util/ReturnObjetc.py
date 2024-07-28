from database.DatabaseOperations import DatabaseOperations
from controller.address_creator import AddressCreator
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
