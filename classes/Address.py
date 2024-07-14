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
        country,
        address_type="Residential",
        notes="",
        is_primary=True,
    ):
        self.id = None
        self.number = number
        self.street = street
        self.postal_code = postal_code
        self.neighborhood = neighborhood
        self.city = city
        self.state = state
        self.country = country
        self.address_type = address_type
        self.notes = notes
        self.is_primary = is_primary
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
