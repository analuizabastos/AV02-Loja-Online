from CadastroEstoque import produtos

estoque = {}
while True:
    print("1. Cadastrar produtos\n2. Ver estoque\n3. Sair\n")
    try:
        escolha2 = int(input("Digite um número: \n"))
        if escolha2 == 1:
            produtos(estoque)
        elif escolha2 == 2:
            print("PRODUTOS NO ESTOQUE\n")
            for nome, info in estoque.items():
                print(f"{nome:<20}R${info['preco']:<10.2f}{info['quantidade']:<10}\n")
        else:
            print("Sessão finalizada.")
            break
    except ValueError:
        print("Digite um valor válido.")