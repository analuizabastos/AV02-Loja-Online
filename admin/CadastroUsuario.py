from services.user_services import buscar_usuario
from services.user_services import cadastro_usuario
from Validacoes.ValidacaoNome import validar_nome
from Validacoes.ValidacaoUsuario import validar_usuario
from Validacoes.ValidacaoSenha import validar_senha
from config.seguranca import criptografar
from services.logs_services import inserir_log
import getpass

def cadastro(conn, id_usuario):
    print("\n---- Cadastro de Usuarios ----")
    while True:
        print("\nUtilize letras, sem caracteres especiais.")
        print("Digite -Sair- para voltar para o Menu Administrativo.")
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
                raise ValueError("Valor inválido. Digite entre 1 ou 2.")
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
        print("\nUtilize letras e numeros, sem espacos ou caracteres especiais.")
        print("Digite -Sair- para voltar para o Menu Principal.")
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
        senha_cadastro = getpass.getpass("Digite a sua senha: ").upper().strip()
        try:
            if senha_cadastro == "SAIR":
                return
            validar_senha(senha_cadastro)
            break
        except ValueError as erro:
            print(erro)
    
    senha_bd = criptografar(senha_cadastro)
    cadastro_banco = cadastro_usuario(conn, nome_cadastro, tipo, usuario_cadastro, senha_bd)
    if cadastro_banco:
        print("Usuario cadastrado com sucesso.\n")
        inserir_log(conn, id_usuario, "CADASTRO_SUCESSO", f"Usuário '{usuario_cadastro}' cadastrado como '{tipo}'.", True)
    else:
        print("Erro ao cadastrar usuário.\n")
        inserir_log(conn, id_usuario, "CADASTRO_FALHA", f"Falha ao cadastrar o usuário '{usuario_cadastro}'.", False)