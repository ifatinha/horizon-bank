from classes.Customer import Customer


class Individual(Customer):

    def __init__(self, fullname, email, telephone, ssn, date_of_birth) -> None:
        super().__init__(fullname, email, telephone)
        self.ssn = ssn
        self.date_of_birth = date_of_birth

    def update(self, **kwargs):
        return super().update(**kwargs)

    def __str__(self) -> str:
        return super().__str__() + f"SSN: {self.ssn}" f"Birthday: {self.date_of_birth}"

    def to_tuple(self):
        return (self.ssn, self.date_of_birth)
