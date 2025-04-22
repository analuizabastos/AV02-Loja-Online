def validar_nome(nome):
    if not nome:
        raise ValueError("Nome inválido. O nome não pode ser espaços vazios.")
    for caractere in nome:
        if not (caractere.isalpha() or caractere == " "):
            raise ValueError("Nome inválido. Use apenas letras.")
    return True