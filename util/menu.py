def main_menu():
    menu = """################ MENU ################
    [1] Cliente
    [2] Admin
    [0] Sair
    => """

    return input(menu)


def manager_menu():
    menu = """################ MENU GERENTE ################
    [1] Novo Cliente
    [2] Nova Conta
    [3] Listar Contas Cliente
    [4] Listar Contas do Banco
    [5] Listar Clientes
    [6] Cadastrar Gerente
    [7] Cadastrar Filial
    [0] Sair
    => """

    return input(menu)


def client_menu():
    menu = """################ MENU CLIENTE ################
    [1] Nova Conta
    [2] Depositar
    [3] Sacar
    [4] Extrato
    [5] Listar Contas
    [0] Sair
    => """

    return input(menu)


def menu_type_customer():
    menu = """################ TIPO DE CLIENTE ################
    [1] Pessoa Física
    [2] Pessoa Juridica
    [0] Sair
    => """

    return input(menu)


def menu_type_account():
    menu = """################ TIPOS DE CONTAS ################
        [1] Poupança
        [2] Corrente
        [3] Empresarial
        [0] Sair
        => """

    return input(menu)


def menu_create_manager():
    menu = """################ CADASTRAR GERENTE ################
        [1] Novo Gerente
        [0] Sair
        => """

    return input(menu)


def menu_create_branch():
    menu = """################ CADASTRAR FILIAL ################
        [1] Nova Filial
        [0] Sair
        => """

    return input(menu)
