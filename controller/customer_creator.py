from controller.address_creator import AddressCreator
from classes.Customer import Customer
from database.customer_db import find_customer_token


class CustomerCreator:

    @staticmethod
    def from_db_record(record):
        address = AddressCreator.from_db_record(record)
        customer = Customer(record[11], record[12], None, record[13], address)

        customer.customer_id = record[10]
        customer.token = record[14]

        return customer
