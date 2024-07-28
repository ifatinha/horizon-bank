from database.customer_db import find_customer_token
from controller.customer_creator import CustomerCreator

customer = find_customer_token("beb31257")
print(CustomerCreator.from_db_record(customer))
