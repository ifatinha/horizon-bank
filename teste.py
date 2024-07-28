from classes.Individual import Individual
from controller.individual_creator import IndividualCreator

individual = IndividualCreator.get_instance()

print(individual.customer_to_tuple())
print(individual.to_tuple())
print(individual.address.to_tuple())
