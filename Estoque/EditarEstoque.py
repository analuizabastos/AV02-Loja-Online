from Estoque.OpcoesEditar import editar_estoque

def editar(estoque):
    if not estoque:
        print("Estoque vazio.")
        return
    
    while True:
        print("Digite -Sair- para voltar para o Menu.\n")
        nome = input("Informe o nome do produto que deseja editar: ").upper().strip()
        if nome == "SAIR":
            break
        if nome not in estoque:
            print("Produto não encontrado, tente novamente.")
            continue
        print(f"produto: {nome}")
        while True:   
            try:
                print("\nO que deseja editar?\n1. Nome\n2. Preço\n3. Quantidade\n4. Sair")
                escolha = int(input("\nDigite o numero:"))
                if escolha in [1,2,3,4]:
                    if escolha == 4:
                        return
                    else:
                        editar_estoque(estoque, nome, escolha)
                        break
                else:
                    print("Valor inválido, digite apenas 1, 2, 3 ou 4.")
                    continue
            except ValueError:
                print("Digite um valor valido.\n")
        
        while True:
            print("Deseja fazer mais alguma alteração?\n1. Sim\n2. Não")
            escolha2 = int(input("\nDigite um numero: "))
            if escolha2 == 1:
                break
            elif escolha2 == 2:
                print("Encerrando...")
                return
            else:
                print("Numero inválido, escolha 1 ou 2")
