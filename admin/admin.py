from admin.CadastroUsuario import cadastro
from admin.EditarUsuario import menu_editar_usuario
from admin.ExcluirUsuario import menu_excluir_usuario
from admin.ListarUsuario import listar_usuarios
def admin_panel(conn):
    while True:
        print("\nPainel do Administrador")
        print("1 - Cadastrar novo usuário")
        print("2 - Editar usuário")
        print("3 - Excluir usuário")
        print("4 - Listar usuários")
        print("5 - Exibir os logs")
        print("6 - Sair")
        
        try:
            escolha = int(input("Digite um numero: "))
            if escolha in [1,2,3,4,5,6]:
                if escolha == 1:
                    cadastro(conn)
                elif escolha == 2:
                    menu_editar_usuario(conn)
                elif escolha == 3:
                    menu_excluir_usuario(conn)
                elif escolha == 4:
                    listar_usuarios(conn)
                elif escolha == 5:
                    pass
                else:
                    print("Sessão finalizada.")
                    return
            else:
                print("Digite um valor do menu.\n")
        except ValueError:
                print("Digite um valor valido.\n")
