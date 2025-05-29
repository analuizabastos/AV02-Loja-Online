from services.user_services import buscar_usuario, excluir_usuario

def menu_excluir_usuario(conn):
    print("\n--- Excluir Usuário ---\n")
    while True:
        print("Digite -Sair- para voltar para o Menu Administrativo.")
    
        login_busca = input("Digite o login do usuário que deseja excluir: ").strip().upper()
        if login_busca == "SAIR":
            return
        resultado = buscar_usuario(conn, login_busca)

        if not resultado:
            print("Usuário não encontrado.")
            return
        
        nome, tipo, login, senha = resultado
        
        while True:
            print(f"\nUsuário atual: Nome: {nome}, Tipo: {tipo}, Login: {login}")
            print("Deseja excluir esse usuario?")
            print("Essa acao nao pode ser revertida.")
            try:
                escolha = int(input("1- Nao;\n 2-Sim."))
                if escolha == 1:
                    break
                elif escolha == 2:
                    if excluir_usuario(conn, login):
                        print("Usuario excluido com sucesso!")
                    else:
                        print("Erro ao excluir usuario.")
                    return
                else:
                    raise ValueError("Valor invalido. Digite entre 1 ou 2.")
            except ValueError as erro:
                print(erro)
