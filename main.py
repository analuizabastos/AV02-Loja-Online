from CadastroUsuario import cadastro
from ValidacaoLogin import login

usuarios = {}
while True:
    print("\n--- Estoque da loja X ---\n")
    print("1.Login\n2-Cadastrar Usuario\n3-Sair\n")
    try:
        escolha = int(input("Digite um numero: "))
        if (escolha == 1 or escolha == 2 or escolha == 3):
            if escolha == 1:
                escolha = login(usuarios)
                
            elif escolha == 2:
                escolha == cadastro(usuarios)
            else:
                print("Obrigada.")
                break
        else:
            print("Digite um valor do menu.\n")
    except ValueError:
        print("Digite um valor valido.\n")
    
