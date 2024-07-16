from classes.Account import Account
from classes.Branch import Branch
from classes.Manager import Manager
from classes.Individual import Individual

manager = Manager("John Doe", "", "", None, "4784")
manager.customer_id = 1

branch = Branch(2015, "Agência Itaporanga", "83 4001-3200", None, manager)
branch.id_branch = 2

client = Individual("Jane Doe", "", "", None, "1245", "14/10/1994")
client.customer_id = 3

account = Account("123456", branch, client)
print(account.to_tuple())
