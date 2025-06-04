from Validacoes.ValidacaoNome import validar_nome
from Validacoes.ValidacaoPreco import validar_preco
from Validacoes.ValidacaoQuantidade import validar_quantidade
from Validacoes.ValidarIdCategoria import validar_idcategoria
from services.estoque_services import adicionar_produtos_bd
from Estoque.MostrarCategorias import mostrar_categorias

def cadastro_produto(conn, id_usuario):
    while True:
        while True:
            print("\nDigite -Sair- para voltar para o Menu.")
            nome_produto = input("\nNome do produto: ").upper()
            try:
                if nome_produto == "SAIR":
                    return
                validar_nome(nome_produto)
                nome = nome_produto
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
                mostrar_categorias(conn)
                print("Digite -Sair- para voltar para o Menu.\n")
                cadastro_categoria = input("Informe a categoria do produto: ").strip()
                if cadastro_categoria.upper() == "SAIR":
                    return
                validar_idcategoria(conn, cadastro_categoria)
                id_categoria = cadastro_categoria
                break
            except ValueError as erro:
                print(erro)
        while True:
            try:
                print("Digite -Sair- para voltar para o Menu.\n")
                quant = (input("Quantidade do produto: ")).strip()
                if quant.upper() == "SAIR":
                    break
                validar_quantidade(quant)
                quantidade = int(quant)
                break
            except ValueError as erro:
                print(erro)
        while True:
            try:
                print("Deseja cadastrar esse produto?\n1. Sim\n2. Não")
                resposta = int(input("Digite um numero: "))
                if resposta == 1:
                    sucesso = adicionar_produtos_bd(conn, nome, quantidade, valor_produto, id_usuario, id_categoria)
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