def login(usuarios):
    contador = 0
    while True:
        print("Se ainda nao possui cadastro, digite -Sair- para voltar para o Menu Principal.\n")
        usuario_temp = input("Digite o usuario: ").upper()
        if usuario_temp in usuarios:
            print("Usuario correto!\n")
            break
        elif usuario_temp == "SAIR":
            return False
        else:
            print("Usuario nao encontrado. Tente Novamente!")
    while contador < 3:
        senha_temp = input("Digite sua senha: ").upper()
        if usuarios[usuario_temp] == senha_temp:
            print("Login validado com sucesso!")
            return True
        elif senha_temp == "SAIR":
            return False
        elif contador == 2:
            print("Senha incorreta. Ultima tentativa.")
        else: 
            print("Senha incorreta. Tente novamente!")
            print("Digite -Sair- para voltar para o Menu Principal.")
            contador+=1
    print("Número máximo de tentativas excedido. Retornando ao menu principal.")
    return False 
    
        
    