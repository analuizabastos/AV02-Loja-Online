from services.user_services import buscar_usuario, editar_usuario
from Validacoes.ValidacaoNome import validar_nome
from Validacoes.ValidacaoUsuario import validar_usuario
from Validacoes.ValidacaoSenha import validar_senha
from services.logs_services import inserir_log
import getpass

def menu_editar_usuario(conn, id_usuario):
    print("\n--- Edição de Usuário ---")
    
    login_busca = input("Digite o login do usuário que deseja editar: ").strip().upper()
    resultado = buscar_usuario(conn, login_busca)
    if not resultado:
        print("Usuário não encontrado.")
        return
    
    id_bd, nome_bd, tipo_bd, login_bd, senha_bd = resultado
    nome_atual = nome_bd
    tipo_atual = tipo_bd
    login_atual = login_bd
    senha_atual = senha_bd
    

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
                    nome_atual = novo_nome
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
                        verificacao = input("Digite 'SIM' ou 'NAO'\nDeseja confirmar? ").upper().strip()
                        if verificacao == "SIM":
                            tipo_atual = "MASTER"
                            break
                        elif verificacao == "NAO":
                            continue
                        else:
                            raise ValueError("Opcao invalida. Digite SIM ou NAO.")
                    else:
                        tipo_atual = "COMUM"
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
                    login_atual = novo_login
                    break
        elif escolha == '4':
            while True:
                print("\nUtilize letras e numeros, sem espacos ou caracteres especiais. Minimo de 6 caracteres.")
                print("Digite -Sair- para voltar para o Menu Editar.\n")
                nova_senha = getpass.getpass("Digite a sua senha: ").upper().strip()
                if nova_senha == "SAIR":
                    break
                try:
                    validar_senha(nova_senha)
                    senha_atual = nova_senha
                    break
                except ValueError as erro:
                    print(erro)
                
        elif escolha == '5':
            alteracoes = editar_usuario(conn, id_bd, nome_atual, tipo_atual, login_atual, senha_atual)
            if alteracoes:
                print("Usuário atualizado com sucesso!")
                campos = []
                for campo in alteracoes:
                    if campo == 'senha':
                        campos.append("Senha alterada")
                    else:
                        valor = locals().get(campo)
                        campos.append(f"{campo} para '{valor}'")
                descricao = f"Usuário '{login_busca}' alterado: " + ", ".join(campos)
                inserir_log(conn, id_usuario, "EDITAR_USUARIO_SUCESSO", descricao, True)
            else:
                descricao = f"Edição do Usuário '{login_busca}' falhou."
                print("Nenhuma alteração realizada ou erro durante a atualização.")
                inserir_log(conn, id_usuario, "EDITAR_USUARIO_FALHA", descricao, False)
            break
        elif escolha == '0':
            print("Edição cancelada.")
            break
        else:
            print("Opção inválida. Tente novamente.")
