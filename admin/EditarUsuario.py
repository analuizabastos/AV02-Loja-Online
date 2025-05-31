from services.user_services import buscar_usuario, editar_usuario
from Validacoes.ValidacaoNome import validar_nome
from Validacoes.ValidacaoNomeUsuario import validar_usuario
from Validacoes.ValidacaoSenha import validar_senha

def menu_editar_usuario(conn):
    print("\n--- Edição de Usuário ---")
    
    login_busca = input("Digite o login do usuário que deseja editar: ").strip().upper()
    resultado = buscar_usuario(conn, login_busca)

    if not resultado:
        print("Usuário não encontrado.")
        return
    
    nome_atual, tipo_atual, login_atual, senha_atual = resultado

    while True:
        print(f"\nUsuário atual: Nome: {nome_atual}, Tipo: {tipo_atual}, Login: {login_atual}")
        print("1 - Editar Nome")
        print("2 - Editar Tipo")
        print("3 - Editar Login")
        print("4 - Editar Senha")
        print("5 - Confirmar e Salvar Alterações")
        print("0 - Sair")

        escolha = input("Digite uma opção: ").strip()

        nome = tipo = login = senha = None

        if escolha == '1':
            while True:
                print("Digite -Sair- para voltar para o Menu Editar.\n")
                novo_nome = input("Digite o novo nome: ").upper()
                if novo_nome == "SAIR":
                    break
                try:
                    validar_nome(novo_nome)
                    nome = novo_nome
                    break 
                except ValueError as erro:
                    print(erro)
        elif escolha == '2':
            while True:
                tipo = int(input("Escolha o novo tipo (1- Master/ 2- Comum)\n: "))
                try:
                    if tipo not in [1,2]:
                        raise ValueError("Valor invalido. Digite entre 1 ou 2.")
                    if tipo == 2:
                        print("Atencao! Usuarios Master tem acesso a todo o sistema.")
                        verificacao = input("Deseja confirmar? Digite 'SIM' ou 'NAO'").upper().strip()
                        if verificacao == "SIM":
                            tipo = "Master"
                            break
                        elif verificacao == "NAO":
                            continue
                        else:
                            raise ValueError("Opcao invalida. Digite SIM ou NAO.")
                    else:
                        tipo = "Comum"
                        break
                except ValueError as erro:
                    print(erro)
        elif escolha == '3':
            while True:
                print("Utilize letras e numeros, sem espacos ou caracteres especiais.")
                print("Digite -Sair- para voltar para o Menu Editar.\n")
                novo_login = input("Digite o novo login: ").strip().upper()
                if novo_login == "SAIR":
                        break
                try:
                    validar_usuario(novo_login)
                except ValueError as erro:
                    print(erro)
                verificacao = buscar_usuario(conn, novo_login)    
                if verificacao:
                    print("Usuario ja cadastrado. Tente novamente!")    
                    continue
                else:
                    login = novo_login
                    break
        elif escolha == '4':
            while True:
                print("\nUtilize letras e numeros, sem espacos ou caracteres especiais. Minimo de 6 caracteres.")
                print("Digite -Sair- para voltar para o Menu Editar.\n")
                nova_senha = input("Digite a sua senha: ").upper().strip()
                if nova_senha == "SAIR":
                    break
                try:
                    validar_senha(nova_senha)
                    senha = nova_senha
                    break
                except ValueError as erro:
                    print(erro)
                
        elif escolha == '5':
            sucesso = editar_usuario(conn, login_busca, nome, tipo, login, senha)
            if sucesso:
                print("Usuário atualizado com sucesso!")
            else:
                print("Nenhuma alteração realizada ou erro durante a atualização.")
            break
        elif escolha == '0':
            print("Edição cancelada.")
            break
        else:
            print("Opção inválida. Tente novamente.")
