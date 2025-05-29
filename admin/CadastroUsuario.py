from services.user_services import buscar_usuario
from services.user_services import cadastro_usuario

def cadastro(conn):
    print("\n---- Cadastro de Usuarios ----")
    while True:
        print("Utilize letras, sem caracteres especiais.")
        print("Digite -Sair- para voltar para o Menu Administrativo.\n")
        nome_cadastro = input("Digite seu nome: ").upper().strip()
        try:    
            for caractere in nome_cadastro:
                if not caractere.isalpha():
                    raise ValueError("Nome invalido. Tente novamente!")
            if not nome_cadastro:
                raise ValueError("Usuário inválido. Não pode ser vazio ou só espaços!\n")
            elif nome_cadastro == "SAIR":
                return
            else:
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
    while True:
        print("Utilize letras e numeros, sem espacos ou caracteres especiais.")
        print("Digite -Sair- para voltar para o Menu Principal.\n")
        usuario_cadastro = input("Digite seu usuario: ").upper().strip()
        try:
            for caractere in usuario_cadastro:
                if not caractere.isalnum():
                    raise ValueError("Usuario invalido. Tente novamente!")
            if not usuario_cadastro:
                raise ValueError("Usuário inválido. Não pode ser vazio ou só espaços!\n")
            verificacao = buscar_usuario(conn, usuario_cadastro)
            if verificacao:
                print("Usuario ja cadastrado. Tente novamente!")    
                continue
            elif usuario_cadastro == "SAIR":
                return
            else:
                break
        except ValueError as erro:
            print(erro)
    while True:
        print("\nUtilize letras e numeros, sem espacos ou caracteres especiais. Minimo de 6 caracteres.")
        senha_cadastro = input("Digite a sua senha: ").upper().strip()
        try:
            for caractere_senha in senha_cadastro:
                if not caractere_senha.isalnum():
                    raise ValueError("Senha com caracteres invalidos. Tente novamente!")
            if len(senha_cadastro) < 6:
                raise ValueError("Senha curta. Tente novamente com, no minimo, 6 caracteres.")
            elif senha_cadastro == "SAIR":
                return
            break
        except ValueError as erro:
            print(erro)
    
    cadastro_banco = cadastro_usuario(conn, nome_cadastro, tipo, usuario_cadastro, senha_cadastro)
    if cadastro_banco:
        print("Usuario cadastrado com sucesso.\n")