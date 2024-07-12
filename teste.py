from classes.Address import Address

address = Address(
    number="1",
    street="Main St",
    city="New York",
    state="NY",
    postal_code="10001",
    country="USA",
    latitude=40.712776,
    longitude=-74.005974,
    address_type="Residential",
    is_primary=True,
    notes="Endereço residencial principal em Nova York",
)

print(address)

address.update(
    city="Los Angeles",
    state="CA",
    postal_code="90001",
    notes="Mudança de endereço para Los Angeles.",
)

print(address)
