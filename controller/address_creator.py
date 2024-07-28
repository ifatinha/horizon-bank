from classes.Address import Address
from classes.AddressTypes import AddressType


class AddressCreator:

    @staticmethod
    def get_address_type():
        address_types = {
            1: AddressType.RESIDENTIAL.value,
            2: AddressType.BUSINESS.value,
            3: AddressType.SHIPPING.value,
            4: AddressType.BILLING.value,
        }

        prompt = "Tipo de Endereço: ('[1] - Residencial', '[2] - Comercial', '[3] - Envio', '[4] - Cobrança'): "

        while True:
            try:
                type_address = int(input(prompt))

                if type_address in address_types:
                    return address_types[type_address]
                else:
                    print("@@@ Opção Inválida, tente novamente. @@@")
            except ValueError:
                print("@@@ Entrada inválida, por favor insira um número. @@@")

    @staticmethod
    def get_instance():
        print("### Informações de Endereço ###")
        street = input("Endereço: ")
        number = input("Número: ")
        neighborhood = input("Bairro: ")
        postal_code = input("CEP: ")
        city = input("Cidade: ")
        state = input("Estado: ")
        address_type = AddressCreator.get_address_type()
        notes = input("Detalhes: ")

        return Address(
            number,
            street,
            postal_code,
            neighborhood,
            city,
            state,
            address_type,
            notes,
        )

    @staticmethod
    def from_db_record(record):
        address = Address(
            record[0],  # number,
            record[1],  # street,
            record[2],  # postal_code,
            record[3],  # neighborhood,
            record[4],  # city,
            record[5],  # state,
            record[7],  # address_type,
            record[9],  # notes,
            record[6],  # country,
            record[8],  # is_primary,
        )

        return address
