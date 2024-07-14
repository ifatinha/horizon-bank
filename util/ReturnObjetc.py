from classes.Address import Address


def return_address():
    street = input("Rua: ")
    number = input("Número: ")
    postal_code = input("CEP: ")
    neighborhood = input("Bairro: ")
    city = input("Cidade: ")
    state = input("Estado: ")
    country = input("Pais: ")

    while True:
        type_address = int(
            input(
                "Tipo de Endereço: ('[1] - Residential', '[2] - Business', '[3] - Shipping', '[4] - Billing'): "
            )
        )

        if type_address == 1:
            address_type = "Residential"
            break
        elif type_address == 2:
            address_type = "Business"
            break
        elif type_address == 3:
            address_type = "Shipping"
            break
        elif type_address == 4:
            address_type = "Billing"
            break
        else:
            print("@@@ Opção Inválida, tente novamente.")

    notes = input("Detalhes: ")

    return Address(
        number,
        street,
        postal_code,
        neighborhood,
        city,
        state,
        country,
        address_type,
        notes,
    )


def return_customer():
    pass
