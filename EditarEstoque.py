def editar(estoque):
    if not estoque:
        print("Estoque vazio")
        return
    
    while True:
        nome = input("Informe o nome do produto que deseja editar: ")
        if nome not in estoque:
            print("Produto não encontrado, tente novamente")
        print(f"produto: {nome}")
        print("\nO que deseja editar?\n1. Nome\n2. Preço\n3. Quantidade")
        escolha = int(input("\nDigite um numero:"))
        if escolha == 1:
            novo_nome = input("Digite um novo nome: ")
            estoque[novo_nome] = estoque.pop(nome)
        elif escolha == 2:
            novo_preco = float(input("Digite o novo preço: "))
            estoque[nome]['preco'] = novo_preco
        elif escolha == 3:
            nova_quantidade = int(input("Digite a nova quantidade: "))
            estoque[nome]['quantidade'] = nova_quantidade
        else:
            print("Valor inválido, digite apenas 1, 2 ou 3")
        while True:
            escolha2 = int(input("Deseja fazer mais alguma alteração?\n1. Sim\n2. Não"))
            if escolha2 == 1:
                break
            elif escolha2 == 2:
                print("Encerrando...")
                return
            else:
                print("Numero inválido, escolha 1 ou 2")
