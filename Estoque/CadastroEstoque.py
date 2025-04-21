from Validacoes.ValidacaoNome import validar_nome
from Validacoes.ValidacaoPreco import validar_preco
from Validacoes.ValidacaoQuantidade import validar_quantidade

def produtos(estoque):
    while True:
        while True:
            nome = input("\nNome do produto: ").upper().strip()
            try:
                validar_nome(nome)
                break 
            except ValueError as erro:
                print(erro) 
        while True:    
            try:    
                preco = float(input("Preço do produto: "))
                validar_preco(preco)
                break
            except ValueError:
                print("Preco invalido. Digite apenas numeros.")   
        
        while True:
            try:
                quantidade = (input("Quantidade do produto: ")).strip()
                validar_quantidade(quantidade)
                break
            except ValueError as erro:
                print(erro)
                
        estoque[nome] = {
            'preco': preco,
            'quantidade': quantidade
        }

        while True:       
            try:
                print("\nDeseja cadastrar um novo produto?\n1. Sim\n2. Não")
                escolha = int(input("\nDigite o numero: "))
                if escolha == 2:
                    print("\n-------------------------------")
                    print("Cadastro de produtos concluido.")
                    print("-------------------------------\n")
                    return False
                elif escolha == 1:
                    break
                else:
                    raise ValueError("Valor inválido. Digite 1 ou 2.")
            except ValueError as erro_numero:
                print(erro_numero)