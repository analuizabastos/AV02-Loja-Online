from services.user_services import buscar_usuario
from services.user_services import cadastro_usuario
from Validacoes.ValidacaoNome import validar_nome
from Validacoes.ValidacaoUsuario import validar_usuario
from Validacoes.ValidacaoSenha import validar_senha

def cadastro(conn):
    print("\n---- Cadastro de Usuarios ----")
    while True:
        print("Utilize letras, sem caracteres especiais.")
        print("Digite -Sair- para voltar para o Menu Administrativo.\n")
        nome_cadastro = input("Digite seu nome: ").upper()
        try:
            if nome_cadastro == "SAIR":
                return
            validar_nome(nome_cadastro)
            break 
        except ValueError as erro:
                print(erro)
    while True: 
        print("Qual o tipo do usuario?\n")
        print("1- Comum")
        print("2- Master\n")
        try:
            tipo = int(input("Digite o numero: ").strip())
            if tipo not in [1,2]:
                raise ValueError("Valor invalido. Digite entre 1 ou 2.")
            if tipo == 2:
                print("Atencao! Usuarios Master tem acesso a todo o sistema.")
                verificacao = input("Deseja confirmar? Digite 'SIM' ou 'NAO'").upper().strip()
                if verificacao == "SIM":
                    tipo = "MASTER"
                    break
                elif verificacao == "NAO":
                    continue
                else:
                    raise ValueError("Opcao invalida. Digite SIM ou NAO.")
            else:
                tipo = "COMUM"
                break
        except ValueError as erro:
            print(erro)
    while True:
        print("Utilize letras e numeros, sem espacos ou caracteres especiais.")
        print("Digite -Sair- para voltar para o Menu Principal.\n")
        usuario_cadastro = input("Digite seu usuario: ").upper().strip()
        try:
            if usuario_cadastro == "SAIR":
                return
            validar_usuario(usuario_cadastro)
            verificacao = buscar_usuario(conn, usuario_cadastro)
            if verificacao:
                print("Usuario ja cadastrado. Tente novamente!")    
                continue
            else:
                break
        except ValueError as erro:
            print(erro)
    while True:
        print("\nUtilize letras e numeros, sem espacos ou caracteres especiais. Minimo de 6 caracteres.")
        senha_cadastro = input("Digite a sua senha: ").upper().strip()
        try:
            if senha_cadastro == "SAIR":
                return
            validar_senha(senha_cadastro)
            break
        except ValueError as erro:
            print(erro)
    
    cadastro_banco = cadastro_usuario(conn, nome_cadastro, tipo, usuario_cadastro, senha_cadastro)
    if cadastro_banco:
        print("Usuario cadastrado com sucesso.\n")