from datetime import datetime


class Customer:

    def __init__(self, fullname, email, telephone, address) -> None:
        self.id = None
        self.fullname = fullname
        self.email = email
        self.telephone = telephone
        self.address = address
        self.created_at = datetime.now()
        self.updated_ate = datetime.now()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        return (
            f"Nome: {self.nome}\n"
            f"Email: {self.email}\n"
            f"Telefone: {self.telephone}\n"
            f"Endereço\n"
            f"{self.address}"
        )
