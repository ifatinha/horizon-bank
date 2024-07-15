from datetime import datetime


class Branch:

    def __init__(self, name, address, manager) -> None:
        self.id = None
        self.branch_name = name
        self.address = address
        self.manager = manager
        self.open_date = datetime.now()

    def __str__(self) -> str:
        return (
            f"Filial: {self.branch_name}\n"
            f"Aberta em: {self.open_date}\n"
            f"Gerente: {self.manager}\n"
            f"Endereço: {self.address}"
        )

    def to_tuple(self):
        return (self.branch_name, self.open_date)
