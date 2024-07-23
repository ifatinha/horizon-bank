from datetime import datetime
import secrets


class Customer:

    def __init__(self, fullname, email, password, phone, address) -> None:
        self.__customer_id = None
        self.fullname = fullname
        self.email = email
        self.password = password
        self.phone = phone
        self.address = address
        self.__token = Customer.generate_token()
        self.created_at = datetime.now()
        self.updated_ate = datetime.now()

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, id_customer):
        self.__customer_id = id_customer

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token):
        self.__token = token

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
        return (self.fullname, self.email, self.token, self.password, self.phone)

    @staticmethod
    def generate_token(length=8):
        token = secrets.token_hex(length // 2)
        return token
