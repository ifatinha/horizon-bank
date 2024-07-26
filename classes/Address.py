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
    def 

    def __str__(self) -> str:
        return (
            f"{self.street} - {self.number}\n"
            f"{self.city}, {self.postal_code} - {self.state}/{self.country}\n"
            f"{self.notes}"
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
    def get_instance():
        print("### Informações de Endereço ###")
        street = input("Endereço: ")
        number = input("Número: ")
        neighborhood = input("Bairro: ")
        postal_code = input("CEP: ")
        city = input("Cidade: ")
        state = input("Estado: ")

        while True:
            type_address = int(
                input(
                    "Tipo de Endereço: ('[1] - Residential', '[2] - Business', '[3] - Shipping', '[4] - Billing'): "
                )
            )

            if type_address == 1:
                address_type = "Residential"
                break
            elif type_address == 2:
                address_type = "Business"
                break
            elif type_address == 3:
                address_type = "Shipping"
                break
            elif type_address == 4:
                address_type = "Billing"
                break
            else:
                print("@@@ Opção Inválida, tente novamente.")

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
