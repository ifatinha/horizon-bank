from datetime import datetime
import secrets


class Customer:

    def __init__(self, fullname, email, password, phone, address) -> None:
        self.__customer_id = None
        self.__fullname = fullname
        self.__email = email
        self.__password = password
        self.__phone = phone
        self.__address = address
        self.__token = self.generate_token()
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, id_customer):
        self.__customer_id = id_customer

    @property
    def fullname(self):
        return self.__fullname

    @fullname.setter
    def fullname(self, fullname):
        self.__fullname = fullname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token):
        self.__token = token

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self.__updated_at = updated_at

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def to_tuple(self):
        return (self.fullname, self.email, self.password, self.token, self.phone)

    @staticmethod
    def generate_token(length=8):
        token = secrets.token_hex(length // 2)
        return token

    def __str__(self) -> str:
        return (
            f"Código de registro: {self.customer_id}\n"
            f"Nome: {self.fullname}\n"
            f"Email: {self.email}\n"
            f"Telefone: {self.phone}\n"
            f"Token: {self.token}\n"
            f"{self.address}"
        )
