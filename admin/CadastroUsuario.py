def cadastro():
    print("\n---- Cadastro de Usuarios ----")
    while True:
        print("Utilize letras e numeros, sem espacos ou caracteres especiais.")
        print("Digite -Sair- para voltar para o Menu Principal.\n")
        usuario_cadastro = input("Digite o nome do seu usuario: ").upper().strip()
        try:
            for caractere in usuario_cadastro:
                if not caractere.isalnum():
                    raise ValueError("Usuario Invalido. Tente novamente!")
            if usuario_cadastro in usuarios:
                print("Usuario ja cadastrado. Tente novamente!")
                continue
            if not usuario_cadastro:
                raise ValueError("Usuário inválido. Não pode ser vazio ou só espaços!\n")
            elif usuario_cadastro == "SAIR":
                return
            else:
                break
        except ValueError as erro:
            print(erro)
    while True:
        print("\nUtilize letras e numeros, sem espacos ou caracteres especiais. Minimo de 6 caracteres.")
        senha_cadastro = input("Digite a sua senha: ").upper().strip()
        try:
            for caractere_senha in senha_cadastro:
                if not caractere_senha.isalnum():
                    raise ValueError("Senha com caracteres invalidos. Tente novamente!")
            if len(senha_cadastro) < 6:
                raise ValueError("Senha curta. Tente novamente com, no minimo, 6 caracteres.")
            elif senha_cadastro == "SAIR":
                return
            break
        except ValueError as erro:
            print(erro)
    
    usuarios[usuario_cadastro] = senha_cadastro
    print("Usuario cadastrado com sucesso.\n")