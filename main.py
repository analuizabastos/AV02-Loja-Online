from CadastroUsuario import cadastro
from Validacoes.ValidacaoLogin import login
from Estoque.MenuEstoque import menuEstoque

usuarios = {}
while True:
    print("\n--- Estoque da loja X ---\n")
    print("1-Login\n2-Cadastrar Usuario\n3-Sair\n")
    try:
        escolha = int(input("Digite um numero: "))
        if escolha in [1,2,3]:
            if escolha == 1:
                acesso = login(usuarios)
                if acesso: 
                    print("Bem-Vindo ao Estoque.\n")
                    menuEstoque()
                else:
                    print("Voltando ao Menu Pincipal...")
            elif escolha == 2:
                cadastro(usuarios)
            else:
                print("Sessão finalizada.")
                exit()
        else:
            print("Digite um valor do menu.\n")
    except ValueError:
        print("Digite um valor valido.\n")
    
