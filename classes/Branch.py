from datetime import datetime


class Branch:

    def __init__(self, number, name, phone, address, manager) -> None:
        self.id = None
        self.number = number
        self.name = name
        self.phone = phone
        self.address = address
        self.manager = manager
        self.open_date = datetime.now()

    def __str__(self) -> str:
        return (
            f"Filial: {self.name}\n"
            f"Aberta em: {self.open_date}\n"
            f"Gerente: {self.manager}\n"
            f"Endereço: {self.address}"
        )

    def to_tuple(self):
        return (
            self.number,
            self.name,
            self.phone,
            self.open_date,
            self.manager.customer_id,
        )
