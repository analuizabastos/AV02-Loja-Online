from CadastroEstoque import produtos

def menuEstoque():
    estoque = {}
    while True:
        print("----Estoque da Loja X----")
        print("O que deseja fazer?")
        print("1. Cadastrar produtos\n2. Ver estoque\n3. Sair\n")
        try:
            escolha2 = int(input("Digite um número: \n"))
            if escolha2 == 1:
                produtos(estoque)
            elif escolha2 == 2:
                print("PRODUTOS NO ESTOQUE\n")
                for nome, info in estoque.items():
                    print(f"Nome:{nome:<20}Preco: R${info['preco']:<10.2f}Quantidade:{info['quantidade']:<10}\n")
            else:
                print("Encerrando...")
                break
        except ValueError:
            print("Digite um valor válido.")