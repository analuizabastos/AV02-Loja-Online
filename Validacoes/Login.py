from services.user_services import buscar_usuario
import bcrypt, getpass
from services.log_services import inserir_log

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
            inserir_log(conn, None, "LOGIN_FALHA", f"Tentativa de login com usuário inexistente '{usuario_bd}'", False)

    while contador < 3:
        senha_temp = getpass.getpass("Digite sua senha: ").strip()
        if senha_temp.upper() == "SAIR":
            return None
        if isinstance(senha_hash, memoryview):
            senha_hash = senha_hash.tobytes()
        elif isinstance(senha_hash, str):
            senha_hash = senha_hash.encode('utf-8')
        senha_bd = bcrypt.checkpw(senha_temp.encode('utf-8'), senha_hash)
        if senha_bd:
            print(f"Login validado com sucesso!")
            inserir_log(conn, id_usuario, "LOGIN_SUCESSO", f"Usuário '{usuario_bd}'", True)
            return {"id": id_usuario, "usuario": nome_bd, "tipo": tipo}
        else:
            contador += 1
            print(f"Senha incorreta. Tentativa {contador}/3.")
            inserir_log(conn, id_usuario, "LOGIN_FALHA", f"Senha incorreta. Tentativa {contador}/3.", False)

    
    print("Número máximo de tentativas excedido.")
    return None

        
    