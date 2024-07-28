def main_menu():
    menu = """################ MENU ################
    [1] Cliente
    [2] Admin
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


def manager_menu():
    menu = """################ MENU GERENTE ################
    [1] Gerenciar Clientes
    [2] Gerenciar Gerentes
    [3] Gerenciar Agências
    [0] Sair
    => """

    return input(menu)


def menu_manager_customers():
    menu = """################ GERENCIAR CLIENTES ################
    [1] Novo Cliente
    [2] Nova Conta
    [3] Clientes Cadastrados
    [4] Buscar Cliente
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
    menu = """################ TIPO DE CONTA ################
    [1] Poupança
    [2] Corrente
    [3] Empresarial
    [0] Sair
    => """

    return input(menu)


def menu_managers():
    menu = """################ GERENCIAR GERENTES ################
    [1] Novo Gerente
    [2] Gerentes Cadastrados
    [0] Sair
    => """

    return input(menu)


def menu_branchs():
    menu = """################ GERENCIAR AGÊNCIAS ################
    [1] Nova Agência
    [2] Agências Cadastradas
    [0] Sair
    => """

    return input(menu)
