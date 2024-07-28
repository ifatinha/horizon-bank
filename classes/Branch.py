from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class Branch:

    number: int
    address: object
    manager: object
    id_branch: int = field(default=None, init=False)
    name: str = field(default="Horizon Bank", init=False)
    phone: str = field(default="0800-123-3001", init=False)
    open_date: datetime = field(default_factory=datetime.now, init=False)

    def __str__(self) -> str:
        return (
            f"Código: {self.id_branch}\n"
            f"Agência: {self.name}\n"
            f"Número da Agência: {self.number}\n"
            f"Telefone: {self.phone}\n"
            f"{self.address}\n"
            f"Gerente: {self.manager.fullname} (Número do Funcionário: {self.manager.employee_number})\n"
            f"Data de Abertura: {self.open_date.strftime('%d/%m/%Y')}"
        )

    def to_tuple(self) -> tuple:
        return (
            self.number,
            self.name,
            self.phone,
            self.open_date,
            self.manager.employee_number,
        )
