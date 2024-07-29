from database.customer_db import find_customer_token
from database.branch_db import find_branch
from controller.account_creator import AccountCreator
from classes.Account import Account

customer = find_customer_token("cdd923f5")
branch = find_branch(1003)

account = AccountCreator.get_instance_savign_account()
print(account.account_bd)
