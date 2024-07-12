from classes.Customer import Customer


class Company(Customer):

    def __init__(self, fullname, email, telephone, ein, legal_name) -> None:
        super().__init__(fullname, email, telephone)
        self.ein = (ein,)
        self.legal_name = legal_name

    def update(self, **kwargs):
        return super().update(**kwargs)

    def __str__(self) -> str:
        return super().__str__() + f"EIN: {self.ein}\n" f"Legal Name: {self.legal_name}"
