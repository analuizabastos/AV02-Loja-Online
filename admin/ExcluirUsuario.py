from services.user_services import buscar_usuario, excluir_usuario
from services.logs_services import inserir_log

def menu_excluir_usuario(conn, id_logado):
    print("\n--- Excluir Usuário ---\n")
    while True:
        print("Digite -Sair- para voltar para o Menu Administrativo.")
    
        login_busca = input("Digite o login do usuário que deseja excluir: ").strip().upper()
        if login_busca == "SAIR":
            return
        resultado = buscar_usuario(conn, login_busca)

        if not resultado:
            print("Usuário não encontrado.")
            inserir_log(conn, id_logado, "EXCLUSAO_FALHA_USUARIO_NAO_ENCONTRADO", f"Tentativa de exclusão falhou: usuário '{login_busca}' não encontrado.", False)
            continue
        
        id_usuario_excluir, nome_excluir, tipo_excluir, login_excluir, senha_excluir = resultado
        
        while True:
            print(f"\nUsuário atual: Nome: {nome_excluir}, Tipo: {tipo_excluir}, Login: {login_excluir}")
            print("Deseja excluir esse usuario?")
            print("Essa ação não pode ser revertida.")
            try:
                escolha = int(input("1- Não\n 2-Sim"))
                if escolha == 1:
                    inserir_log(conn, id_logado, "EXCLUSAO_CANCELADA", f"Exclusão do usuário '{login_excluir}' (ID: {id_usuario_excluir}) cancelada por escolha do usuário.", False)
                    break
                elif escolha == 2:
                    if excluir_usuario(conn, login_excluir):
                        print("Usuario excluido com sucesso!")
                        inserir_log(conn, id_logado, "EXCLUSAO_SUCESSO", f"Usuário '{login_excluir}' (ID: {id_usuario_excluir}) excluído com sucesso.", True)
                    else:
                        print("Erro ao excluir usuario.")
                        inserir_log(conn, id_logado, "EXCLUSAO_FALHA", f"Falha ao excluir o usuário '{login_excluir}' (ID: {id_usuario_excluir}).", False)
                    return
                else:
                    raise ValueError("Valor invalido. Digite entre 1 ou 2.")
            except ValueError as erro:
                print(erro)
