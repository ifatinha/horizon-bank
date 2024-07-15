from classes.Customer import Customer
from classes.Manager import Manager

manager = Manager("John Doe", "johndoe@email.com", "8398153-5656", None, 1, True)

print(manager.to_tuple())
print(manager.super_to_tuple())
