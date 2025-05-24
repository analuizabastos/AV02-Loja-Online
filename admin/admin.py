from admin.CadastroUsuario import cadastro

def admin_panel():
    while True:
        print("Painel do Administrador")
        print("1 - Cadastrar novo usuário")
        print("2 - Editar usuário")
        print("3 - Excluir usuário")
        print("4 - Exibir os logs")
        print("5 - Sair")
        
        try:
            escolha = int(input("Digite um numero: "))
            if escolha in [1,2,3,4,5]:
                if escolha == 1:
                    cadastro()
                elif escolha == 2:
                    pass
                elif escolha == 3:
                    pass
                elif escolha == 4:
                    pass
                else:
                    print("Sessão finalizada.")
                    exit()
            else:
                print("Digite um valor do menu.\n")
        except ValueError:
                print("Digite um valor valido.\n")
