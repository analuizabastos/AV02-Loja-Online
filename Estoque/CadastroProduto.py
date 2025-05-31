from Validacoes.ValidacaoNome import validar_nome
from Validacoes.ValidacaoPreco import validar_preco
from Validacoes.ValidacaoQuantidade import validar_quantidade
from services.estoque_services import adicionar_produtos

def produtos(conn, id_usuario):
    while True:
        while True:
            print("Digite -Sair- para voltar para o Menu.\n")
            nome = input("\nNome do produto: ").upper()
            try:
                if nome == "SAIR":
                    return
                validar_nome(nome)
                nome_produto = nome
                break 
            except ValueError as erro:
                print(erro) 
        while True:    
            try:    
                print("Digite -Sair- para voltar para o Menu.\n")
                preco = input("Preço do produto: ").upper()
                if preco == "SAIR":
                    return
                preco = float(preco)
                validar_preco(preco)
                valor_produto = preco
                break
            except ValueError:
                print("Preco invalido. Digite apenas numeros.")
        while True:
            try:
                print("---------- CATEGORIAS -----------\n")
                print("1 - Eletronicos\n")
                print("2 - Livros\n")
                print("3 - Roupas\n")
                print("Digite -Sair- para voltar para o Menu.\n")
                cadastro_categoria = input("Informe a categoria do produto: ").strip()
                if cadastro_categoria.upper() == "SAIR":
                    return
                categoria_produto = int(cadastro_categoria)
                if categoria_produto in [1,2,3]:
                    if categoria_produto == 1:
                        id_categoria = 1
                        break
                    elif categoria_produto == 2:
                        id_categoria = 2
                        break
                    else:
                        id_categoria = 3
                        break
            except ValueError:
                print("Digite um valor válido")
        while True:
            try:
                quantidade = (input("Quantidade do produto: ")).strip()
                if quantidade.upper() == "SAIR":
                    return
                validar_quantidade(quantidade)
                break
            except ValueError as erro:
                print(erro)
        while True:
            try:
                print("Deseja cadastrar esse produto?\n1. Sim\n2. Não")
                resposta = int(input("Digite um numero: "))
                if resposta == 1:
                    sucesso = adicionar_produtos(conn, nome_produto, quantidade, valor_produto, id_usuario, id_categoria)
                    if sucesso:
                        print("Produto cadastrado com sucesso")
                        break
                    else:
                        print("Erro ao cadastrar o produto.")
                        break
                elif resposta == 2:
                    print("Cadastro cancelado.")
                    break
                else:
                    raise ValueError("Valor inválido. Digite 1 ou 2.")
            except ValueError as erro_numero:
                print(erro_numero)
            
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