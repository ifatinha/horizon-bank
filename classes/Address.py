from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
from enums.AddressTypes import AddressType


@dataclass
class Address:

    number: str
    street: str
    postal_code: str
    neighborhood: str
    city: str
    state: str
    address_type: AddressType = AddressType.RESIDENTIAL.value
    notes: str = ""
    country: str = field(default="Brasil", init=False)
    is_primary: bool = True
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    id: Optional[int] = field(default=None)

    def __post_init__(self):
        self.updated_at = datetime.now()

    def __str__(self):
        return (
            f"Endereço: {self.street}, {self.number}\n"
            f"Bairro: {self.neighborhood}\n"
            f"CEP: {self.postal_code}\n"
            f"Cidade: {self.city} - {self.state}/{self.country}\n"
            f"Tipo: {self.address_type}\n"
            f"Principal: {'Sim' if self.is_primary else 'Não'}\n"
            f"Detalhes: {self.notes if self.notes else ''}"
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
