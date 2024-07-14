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

# last_address_id = cursor.lastrowid
