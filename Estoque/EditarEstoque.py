from Validacoes.ValidacaoNome import validar_nome
from Validacoes.ValidacaoPreco import validar_preco
from Validacoes.ValidacaoQuantidade import validar_quantidade

def editar(estoque):
    if not estoque:
        print("Estoque vazio.")
        return
    
    while True:
        nome = input("Informe o nome do produto que deseja editar: ").upper().strip()
        if nome not in estoque:
            print("Produto não encontrado, tente novamente.")
            continue
        print(f"produto: {nome}")
        while True:   
            try:
                print("\nO que deseja editar?\n1. Nome\n2. Preço\n3. Quantidade\n4. Sair")
                escolha = int(input("\nDigite o numero:"))
                if escolha in [1,2,3,4]:
                    if escolha == 1:
                        while True:
                            try:
                                novo_nome = input("Digite um novo nome: ").upper().strip()
                                validar_nome(novo_nome)
                                if novo_nome not in estoque:
                                    estoque[novo_nome] = estoque.pop(nome)
                                    break
                                else:
                                    raise ValueError("Produto já existe. Digite um novo nome.")
                            except ValueError as erro:
                                print(erro)
                    elif escolha == 2:
                        while True:
                            try: 
                                novo_preco = float(input("Digite o novo preço: "))
                                validar_preco(novo_preco)
                                estoque[nome]['preco'] = novo_preco
                                break
                            except ValueError:
                                print("Preco inválido. Digite apenas números.")
                    elif escolha == 3:
                        while True:
                            try:
                                nova_quantidade = input("Digite a nova quantidade: ")
                                validar_quantidade(nova_quantidade)
                                estoque[nome]['quantidade'] = nova_quantidade
                                break
                            except ValueError as erro:
                                print(erro)
                    else:
                        break
                else:
                    print("Valor inválido, digite apenas 1, 2 ou 3")
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
