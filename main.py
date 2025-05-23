from Validacoes.ValidacaoLogin import login
from Estoque.MenuEstoque import menuEstoque
from config.db import criar_conexao

conn = criar_conexao() 
if conn is None:
    print("Erro ao conectar ao banco. Encerrando sistema.")
    exit()

while True:
    print("\n--- Estoque da loja X ---\n")
    print("1-Login\n2-Sair\n")
    try:
        escolha = int(input("Digite um número: "))
        if escolha == 1:
            acesso = login(conn)
            if acesso: 
                print(f"\nBem-vindo ao sistema, {acesso['usuario']} ({acesso['tipo']})\n")
                menuEstoque(conn)
            else:
                print("Voltando ao Menu Principal...")
        elif escolha == 2:
            print("Sessão finalizada.")
            conn.close()
            exit()
        else:
            print("Digite um valor do menu.\n")
    except ValueError:
        print("Digite um valor válido.\n")
    
