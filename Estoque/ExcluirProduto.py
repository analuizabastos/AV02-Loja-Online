from Validacoes.ValidacaoNome import validar_nome

def RemoverProduto(estoque): 
    if not estoque:
        print("Estoque vazio.")
        return
    while True:
        try:   
            nome = input("Informe o nome do produto que deseja excluir: ").upper().strip()
            validar_nome(nome)
            if nome in estoque:
                estoque.pop(nome)
                print("\n-----------------------------------------")
                print(f"{nome} foi removido do estoque com sucesso.")
                print("-----------------------------------------")
                break
            else:
                print("Produto não encontrado, tente novamente.")
                continue
        except ValueError as erro:
            print(erro)
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
