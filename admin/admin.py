from admin.CadastroUsuario import cadastro
from admin.EditarUsuario import menu_editar_usuario
from admin.ExcluirUsuario import menu_excluir_usuario
def admin_panel(conn):
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
                    cadastro(conn)
                    continue
                elif escolha == 2:
                    menu_editar_usuario(conn)
                    continue
                elif escolha == 3:
                    menu_excluir_usuario(conn)
                    continue
                elif escolha == 4:
                    pass
                else:
                    print("Sessão finalizada.")
                    exit()
            else:
                print("Digite um valor do menu.\n")
        except ValueError:
                print("Digite um valor valido.\n")
