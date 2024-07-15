from datetime import datetime


class Customer:

    def __init__(self, fullname, email, phone, address) -> None:
        self.id = None
        self.fullname = fullname
        self.email = email
        self.phone = phone
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
            f"Nome: {self.fullname}\n"
            f"Email: {self.email}\n"
            f"Telefone: {self.phone}\n"
            f"Endereço\n"
            f"{self.address}"
        )

    def to_tuple(self):
        return (self.fullname, self.email, self.phone)
