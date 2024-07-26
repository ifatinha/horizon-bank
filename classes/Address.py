from datetime import datetime


class Address:

    def __init__(
        self,
        number,
        street,
        postal_code,
        neighborhood,
        city,
        state,
        address_type="Residential",
        notes="",
        is_primary=True,
    ):
        self.__id = None
        self.__number = number
        self.__street = street
        self.__postal_code = postal_code
        self.__neighborhood = neighborhood
        self.__city = city
        self.__state = state
        self.__country = "Brasil"
        self.__address_type = address_type
        self.__notes = notes
        self.__is_primary = is_primary
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()

    @property
    def id(self):
        return self.__id

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street):
        self.__street = street

    @property
    def postal_code(self):
        return self.__postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        self.__postal_code = postal_code

    @property
    def neighborhood(self):
        return self.__neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood):
        self.__neighborhood = neighborhood

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        self.__country = country

    @property
    def address_type(self):
        return self.__address_type

    @address_type.setter
    def address_type(self, address_type):
        self.__address_type = address_type

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, notes):
        self.__notes = notes

    @property
    def is_primary(self):
        return self.__is_primary

    @is_primary.setter
    def is_primary(self, is_primary):
        self.__is_primary = is_primary

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at

    def __str__(self):
        return (
            f"Endereço: {self.street}, {self.number}\n"
            f"Bairro: {self.neighborhood}\n"
            f"CEP: {self.postal_code}\n"
            f"Cidade: {self.city} - {self.state}\n"
            f"Tipo: {self.address_type}\n"
            f"Principal: {self.is_primary}\n"
            f"Detalhes: {self.notes}"
        )

    def to_tuple(self) -> str:
        return (
            self.number,
            self.street,
            self.postal_code,
            self.neighborhood,
            self.city,
            self.state,
            self.country,
            self.address_type,
            self.is_primary,
            self.notes,
        )

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    @staticmethod
    def get_address_type():
        address_types = {1: "Residential", 2: "Business", 3: "Shipping", 4: "Billing"}

        while True:
            try:
                type_address = int(
                    input(
                        "Tipo de Endereço: ('[1] - Residêncial', '[2] - Comercial', '[3] - Envio', '[4] - Cobrança'): "
                    )
                )

                if type_address in address_types:
                    return address_types[type_address]
                else:
                    print("@@@ Opção Inválida, tente novamente. @@@")
            except ValueError:
                print("@@@ Entrada inválida, por favor insira um número. @@@")

    @staticmethod
    def get_instance():
        print("### Informações de Endereço ###")
        street = input("Endereço: ")
        number = input("Número: ")
        neighborhood = input("Bairro: ")
        postal_code = input("CEP: ")
        city = input("Cidade: ")
        state = input("Estado: ")
        address_type = Address.get_address_type()
        notes = input("Detalhes: ")

        return Address(
            number,
            street,
            postal_code,
            neighborhood,
            city,
            state,
            address_type,
            notes,
        )

    @staticmethod
    def from_db_record(result):
        return Address(
            result[0],
            result[1],
            result[2],
            result[4],
            result[5],
            result[6],
            result[7],
            result[8],
            result[9],
            result[10],
        )
