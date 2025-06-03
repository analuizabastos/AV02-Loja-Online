from admin.CadastroUsuario import cadastro
from admin.EditarUsuario import menu_editar_usuario
from admin.ExcluirUsuario import menu_excluir_usuario
from admin.ListarUsuario import listar_usuarios
from admin.ListarLogs import listar_logs

def admin_panel(conn, id_usuario):
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
                    cadastro(conn, id_usuario)
                elif escolha == 2:
                    menu_editar_usuario(conn, id_usuario)
                elif escolha == 3:
                    menu_excluir_usuario(conn, id_usuario)
                elif escolha == 4:
                    listar_usuarios(conn)
                elif escolha == 5:
                    listar_logs(conn)
                else:
                    print("Sessão finalizada.")
                    return
            else:
                print("Digite um valor do menu.\n")
        except ValueError:
                print("Digite um valor valido.\n")
