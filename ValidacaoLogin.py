def login(usuarios):
    contador = 0
    while True:
        usuario_temp = input("Digite o usuario: ").upper()
        if usuario_temp in usuarios:
            print("Usuario correto!")
            break
        elif usuario_temp == "SAIR":
            return False
        else:
            print("Usuario nao encontrado. Tente Novamente!")
            print("Se ainda nao possui cadastro, digite -Sair- para voltar para o Menu Principal.")
    while contador <= 4:
        senha_temp = input("Digite sua senha: ").upper()
        if usuarios[usuario_temp] == senha_temp:
            print("Login validado com sucesso!")
            return True
        elif senha_temp == "SAIR":
            return False
        else: 
            print("Senha incorreta. Tente novamente!")
            print("Digite -Sair- para voltar para o Menu Principal.")
            contador+=1
    
        
    