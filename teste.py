from classes.Customer import Customer
from classes.Manager import Manager
from datetime import datetime

##manager = Manager("John Doe", "johndoe@email.com", "8398153-5656", None, 1, True)
customer = Customer("Jane Doe", "janedoe@email.com", "83 9856-8956", None)

customer.customer_id = 1
print(customer.customer_id)

print(datetime.now())
