from services.user_services import buscar_usuario
import bcrypt

def login(conn):
    contador = 0
    while True:
        print("Se ainda não possui cadastro, digite -SAIR- para voltar ao menu principal.")
        usuario_bd = input("Digite o nome de usuário: ").strip().upper()
        if usuario_bd == "SAIR":
            return None
        resultado = buscar_usuario(conn, usuario_bd)
        if resultado:
            id_usuario, nome_bd, tipo, usuario_bd, senha_hash = resultado
            break
        else:
            print("Usuário não encontrado. Tente novamente.")
    while contador < 3:
        senha_temp = input("Digite sua senha: ").strip()
        if senha_temp.upper() == "SAIR":
            return None
        senha_bd = bcrypt.checkpw(
        senha_temp.encode('utf-8'),
        senha_hash.tobytes() if isinstance(senha_hash, memoryview) else senha_hash.encode('utf-8'))
        if senha_bd:
            print(f"Login validado com sucesso!")
            return {"id": id_usuario, "usuario": nome_bd, "tipo": tipo}
        else:
            contador += 1
            print(f"Senha incorreta. Tentativa {contador}/3.")
    
    print("Número máximo de tentativas excedido.")
    return None

        
    