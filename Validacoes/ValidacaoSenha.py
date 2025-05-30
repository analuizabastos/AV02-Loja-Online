def validar_senha(senha):
    for caractere_senha in senha:
        if not caractere_senha.isalnum():
            raise ValueError("Senha com caracteres invalidos. Tente novamente!")
    if len(senha) < 6:
        raise ValueError("Senha curta. Tente novamente com, no minimo, 6 caracteres.")