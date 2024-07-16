from classes.Customer import Customer
from classes.Manager import Manager
from datetime import datetime
import random


def generate_account_number():
    now = datetime.now()
    date_str = now.strftime("%Y%m%d%H%M%S")
    random_number = random.randint(1, 1000)
    return f"{date_str}{random_number}"


def generate_us_account_number():

    # Número da conta – 10 dígitos
    account_number = f"{random.randint(1000000000, 9999999999)}"

    return account_number


print(generate_account_number())
print(generate_us_account_number())
