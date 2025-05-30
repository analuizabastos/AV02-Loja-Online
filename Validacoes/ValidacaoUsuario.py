def validar_usuario(usuario):
    for caractere in usuario:
        if not caractere.isalnum():
            raise ValueError("Usuario invalido. Tente novamente!")
    if not usuario:
        raise ValueError("Usuário inválido. Não pode ser vazio ou só espaços!\n")