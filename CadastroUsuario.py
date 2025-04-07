def cadastro(usuarios):
    print("---- Cadastro de Usuarios ----")
    while True:
        print("Utilize letras e numeros, sem caracteres especiais.")
        usuario_cadastro = input("Digite o nome do seu usuario: ").upper()
        if usuario_cadastro in usuarios:
            print("Usuario ja cadastrado. Tente novamente!")
        else:
            break
    while True:
        print("Utilize letras e numeros, sem caracteres especiais. Minimo de 6 caracteres.")
        senha_cadastro = input("Digite a sua senha: ").upper()
        if len(senha_cadastro) < 6:
            print("Tente novamente!")
        else:
            break
    
    usuarios[usuario_cadastro] = senha_cadastro
    print("Usuario cadastrado com sucesso.")