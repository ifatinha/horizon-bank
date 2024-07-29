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


def return_transaction_Deposit(historic_id, value):
    deposit = Deposit(value)
    return deposit.to_tuple() + (historic_id,)


def return_transaction_Withdraw(historic_id, value):
    withdraw = Withdraw(value)
    return withdraw.to_tuple() + (historic_id,)


def return_transaction_transfer(historic_id, value):
    transfer = Transfer(value)
    return transfer.to_tuple() + (historic_id,)
