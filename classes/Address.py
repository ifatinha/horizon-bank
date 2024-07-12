from datetime import datetime


class Address:

    def __init__(
        self,
        number,
        street,
        city,
        state,
        postal_code,
        country,
        latitude=None,
        longitude=None,
        address_type="Residential",
        is_primary=False,
        notes="",
    ):
        self.id = None
        self.number = number
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.address_type = address_type
        self.is_primary = is_primary
        self.notes = notes
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        return (
            f"{self.street} - {self.number}\n"
            f"{self.city}, {self.postal_code} - {self.state}/{self.country}\n"
            f"{self.notes}"
        )

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
