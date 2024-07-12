class Branch:

    def __init__(self, name, address, manager, open_date) -> None:
        self.id = None
        self.name = name
        self.address = address
        self.manager = manager
        self.open_date = open_date

    def __str__(self) -> str:
        return (
            f"Filial: {self.name}\n"
            f"Aberta em: {self.open_date}\n"
            f"Gerente: {self.manager}\n"
            f"Endereço: {self.address}"
        )
