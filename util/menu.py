def main_menu():
    menu = """################ MENU ################
    [c] Cliente
    [m] Gerente
    [s] Sair
    => """

    return input(menu)


def menu_manager():
    menu = """################ MENU ################
    [c] Novo Cliente
    [n] Nova Conta
    [l] Listar Contas Cliente
    [m] Listar Contas do Banco
    [p] Listar Clientes
    [q] Sair
    => """

    return input(menu)


def client_menu():
    menu = """################ MENU ################
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Nova Conta
    [l] Listar Contas
    [q] Sair
    => """

    return input(menu)
