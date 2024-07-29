from admin.banking_operations import BankingOperations
from controller.account_creator import AccountCreator
from database.account_db import find_account

account = find_account(6620287101, "1515")
record = AccountCreator.from_db_record(account)
print(record)
