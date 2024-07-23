import secrets


def generate_token(length=8):
    # Gera um token de comprimento especificado (32 caracteres por padrão)
    token = secrets.token_hex(length // 2)
    return token


# Gera um token de 32 caracteres
token = generate_token()
print(f"Token: {token}")
