def cadastro(usuarios):
    print("---- Cadastro de Usuarios ----")
    while True:
        print("Utilize letras e numeros, sem espacos ou caracteres especiais.")
        usuario_cadastro = input("Digite o nome do seu usuario: ").upper()
        try:
            for caractere in usuario_cadastro:
                if not caractere.isalnum():
                    raise ValueError("Usuario Invalido. Tente novamente!")
            if usuario_cadastro in usuarios:
                print("Usuario ja cadastrado. Tente novamente!")
            else:
                break
        except ValueError as erro:
            print(erro)
    while True:
        print("Utilize letras e numeros, sem espacos ou caracteres especiais. Minimo de 6 caracteres.")
        senha_cadastro = input("Digite a sua senha: ").upper()
        try:
            for caractere_senha in senha_cadastro:
                if not caractere_senha.isalnum():
                    raise ValueError("Senha com caracteres invalidos. Tente novamente!")
            if len(senha_cadastro) < 6:
                raise ValueError("Senha curta. Tente novamente com, no minimo, 6 caracteres.")
            break
        except ValueError as erro:
            print(erro)
    
    usuarios[usuario_cadastro] = senha_cadastro
    print("Usuario cadastrado com sucesso.")