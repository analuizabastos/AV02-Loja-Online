from Services.user_services import buscar_usuario

def login(conn):
    contador = 0
    while True:
        print("Se ainda não possui cadastro, digite -SAIR- para voltar ao menu principal.")
        usuario_temp = input("Digite o nome de usuário: ").strip().upper()
        if usuario_temp == "SAIR":
            return None
        resultado = buscar_usuario(conn, usuario_temp)
        if resultado:
            nome_bd, tipo, usuario_bd, senha_bd = resultado
            break
        else:
            print("Usuário não encontrado. Tente novamente.")
    while contador < 3:
        senha_temp = input("Digite sua senha: ").strip()
        if senha_temp == senha_bd:
            print(f"Login validado com sucesso! Tipo de usuário: {tipo}")
            return {"usuario": nome_bd, "tipo": tipo}
        elif senha_temp.upper() == "SAIR":
            return None
        else:
            contador += 1
            print(f"Senha incorreta. Tentativa {contador}/3.")
    print("Número máximo de tentativas excedido.")


        
    