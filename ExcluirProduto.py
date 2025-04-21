def RemoverProduto(estoque): 
    while True:
        nome = input("Informe o nome do produto que deseja excluir: ")
        if nome in estoque:
            estoque.pop(nome)
            print("\n-----------------------------------------")
            print(f"{nome} foi removido do estoque com sucesso.")
            print("-----------------------------------------")
        else:
            print("Produto não encontrado, tente novamente.")
        while True:
            try:
                print("\nDeseja remover mais algum item?\n1. Sim\n2. Não")
                numero = int(input("\nDigite um numero: "))
                if numero == 1:  
                    break
                elif numero == 2:
                    print("Encerrando...")
                    return
                else:
                    print("Numero inválido, digite 1 ou 2")
            except ValueError:
                print("Resposta inválida, digite apenas 1 ou 2")
