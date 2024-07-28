from classes.Customer import Customer


class Individual(Customer):

    def __init__(
        self, fullname, email, password, phone, address, ssn, date_of_birth
    ) -> None:
        super().__init__(fullname, email, password, phone, address)
        self.ssn = ssn
        self.date_of_birth = date_of_birth

    def update(self, **kwargs):
        super().update(**kwargs)
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        return (
            f"Código de registro: {self.customer_id}\n"
            f"Nome: {self.fullname}\n"
            f"Email: {self.email}\n"
            f"Telefone: {self.phone}\n"
            f"{self.address}\n"
            f"SSN: {self.ssn}\n"
            f"Data de nascimento: {self.date_of_birth.strftime('%d/%m/%Y')}"
        )

    def to_tuple(self):
        return (self.ssn, self.date_of_birth)

    def customer_to_tuple(self):
        return super().to_tuple()
