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
    [3] Contas Cliente
    [4] Listar Clientes
    [5] Cadastrar Gerente
    [6] Gerentes Cadastrados
    [7] Cadastrar Agência
    [8] Agências Cadastradas
    [0] Sair
    => """

    return input(menu)


def client_menu():
    menu = """################ MENU CLIENTE ################
    [1] Operações Bancárias
    [2] Suas Contas
    [0] Sair
    => """

    return input(menu)


def menu_banking_operations():
    menu = """################ OPERAÇÕES BANCÁRIAS ################
    [1] Depósito
    [2] Saque
    [3] Transferência
    [4] Extrato
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


def menu_typle_customers():
    menu = """################ CLIENTES CADASTRADOS ################
        [1] Pessoas Fisicas
        [2] Pessoas Juridicas
        [0] Sair
        => """

    return input(menu)
