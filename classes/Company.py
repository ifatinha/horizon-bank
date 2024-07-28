from classes.Customer import Customer


class Company(Customer):

    def __init__(
        self, fullname, email, password, phone, address, ein, legal_name
    ) -> None:
        super().__init__(fullname, email, password, phone, address)
        self.ein = ein
        self.legal_name = legal_name

    def update(self, **kwargs):
        super().update(**kwargs)
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        return (
            f"Código de registro: {self.customer_id}\n"
            f"Razão Social: {self.fullname}\n"
            f"Nome Fantasia: {self.legal_name}\n"
            f"EIN: {self.ein}\n"
            f"Email: {self.email}\n"
            f"Telefone: {self.phone}\n"
            f"{self.address}"
        )

    def to_tuple(self):
        return (self.ein, self.legal_name)

    def customer_to_tuple(self):
        return super().to_tuple()
