from services.user_services import lista_de_usuarios

def listar_usuarios(conn):
    print("-" * 100)
    print("                                Usuários Cadastrados")
    print("-" * 100)

    usuarios = lista_de_usuarios(conn)
    if usuarios:
        print(f"\n{'ID':<5} {'NOME':<20} {'TIPO':<10} {'LOGIN':<15}")
        print("-" * 50)
        for id_usuario, nome, tipo, login in usuarios:
            print(f"{id_usuario:<5} {nome:<20} {tipo:<10} {login:<15}")
    else:
        print("Nenhum usuário cadastrado.")