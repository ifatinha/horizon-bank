from datetime import datetime


class Branch:

    def __init__(self, number, address, manager) -> None:
        self.__id_branch = None
        self.number = number
        self.__name = "Horizon Bank"
        self.phone = "0800-123-3001"
        self.address = address
        self.manager = manager
        self.open_date = datetime.now()

    @property
    def id_branch(self):
        return self.__id_branch

    @id_branch.setter
    def id_branch(self, id_branch):
        self.__id_branch = id_branch

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

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
            self.manager.employee_number,
        )
