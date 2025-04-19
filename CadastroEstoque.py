def produtos(estoque):
    while True:
        print("Escolha a parte de vesturario que deseja cadastrar ")
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade do produto: "))

        estoque[nome] = {
            'preco': preco,
            'quantidade': quantidade
        }

        print("Deseja cadastrar um novo produto?\n1. Sim\n2. Não")
        try:
            escolha = int(input("Digite o numero: "))
            if escolha == 2:
                print("Cadastro de produtos concluido")
                return False
        except ValueError:
            print("Valor inválido, continuado a adição de produtos")