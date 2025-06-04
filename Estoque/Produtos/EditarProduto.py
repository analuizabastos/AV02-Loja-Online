from services.estoque_services import editar_estoque
from Validacoes.ValidacaoNome import validar_nome
from Validacoes.ValidacaoPreco import validar_preco
from Validacoes.ValidacaoQuantidade import validar_quantidade
from services.estoque_services import buscar_produto, buscar_produto_id

def editar_produto(conn):
    while True:
        novo_nome = None
        nova_quantidade = None
        novo_preco = None
        nova_categoria = None
        produto_selecionado = None
        while True:
            print("Digite -Sair- para voltar para o Menu.\n")
            try:
                busca = input("Informe o nome do produto que deseja editar: ").strip()
                if busca.upper() == "SAIR":
                    return
                resultado = buscar_produto(conn, busca)
                if not resultado:
                    print("Produto não encontrado. Tente novamente!")
                    continue
                if len(resultado) > 1:
                    print("Por favor, selecione pelo ID:")
                    print(f"\n{'ID':<5} {'NOME':<30} {'QUANTIDADE':<12} {'VALOR':<10}")
                    for produtos in resultado:
                        id_prod, nome_prod, qtd_prod, valor_prod, _, _ = produtos
                        print(f"{id_prod:<5} {nome_prod:<30} {qtd_prod:<12} {valor_prod:<10.2f}")
                    while True:
                        try:
                            id_produto = input("Digite o ID do produto que deseja editar (SAIR para cancelar): ").strip()
                            if id_produto.upper == "SAIR":
                                print("Edição de produto cancelada.")
                                return
                            id_produto = int(id_produto)
                            produto_selecionado = buscar_produto_id(conn, id_produto)
                            if produto_selecionado:
                                break
                            else:
                                print("ID inválido. Tente novamente!")
                        except ValueError:
                            print("Entrada inválida. Digite um número.")
                else:
                    produto_selecionado = resultado
                    break
            except ValueError:
                print("Digite um numero válido")
        while True:
            print("=" * 50)
            print("O que quer editar?")
            print("=" * 50)
            print("1 - Nome\n2 - Quantidade\n3 - Valor\n4 - Categoria\n 0 - Concluir e salvar alterações.\nDigite -Sair- para voltar para o Menu.")
            try:
                campo = input("Digite um número: ").strip()
                if campo.upper() == "SAIR":
                    break
                campo = int(campo)
                if campo in [0,1,2,3,4]:
                    if campo == 0:
                        break
                    elif campo == 1:
                        while True:
                            nome = input("Informe o novo nome para o produto: ").upper()
                            try:
                                validar_nome(nome)
                                novo_nome = nome
                                break 
                            except ValueError as erro:
                                print(erro) 
                    elif campo == 2:
                        while True:    
                            try:
                                quantidade = (input("Quantidade do produto: ")).strip()
                                validar_quantidade(quantidade)
                                nova_quantidade = int(quantidade)
                                break
                            except ValueError as erro:
                                print(erro)
                    elif campo == 3:
                        while True:    
                            try:    
                                preco = input("Preço do produto: ").upper()
                                novo_preco = float(preco)
                                validar_preco(novo_preco)
                                break
                            except ValueError:
                                print("Preco invalido. Digite apenas numeros.")
                    elif campo == 4:
                        while True:
                            try:
                                print("---------- CATEGORIAS -----------\n")
                                print("1 - Eletronicos\n")
                                print("2 - Livros\n")
                                print("3 - Roupas\n")
                                nova_categoria = int(input("Digite um número: "))
                                if nova_categoria in [1,2,3]:
                                    break
                                else:
                                    print("Número inválido. Digite 1, 2 ou 3.")
                                    continue
                            except ValueError:
                                print("Valor Invalido. Digite um número do menu.")
                    else:
                        print("Número Inválido. Digite um valor do menu.")
            except ValueError:
                    print("Valor inválido. Tente novamente.")
            while True:
                try:
                    print("Deseja salvar essa alterações? \n1 - Sim \n2 - Não")
                    opcao = int(input("Digite um número: "))
                    if opcao == 1:
                        sucesso = editar_estoque(conn, id_produto, novo_nome, nova_quantidade, novo_preco, nova_categoria)
                        if sucesso:
                            print("Produto editado com sucesso!")
                            break
                        else:
                            print("Erro ao editar produto.")
                    elif opcao == 2:
                        print("Edição cancelada.")
                        break
                except ValueError:
                    print("Valor inválido.")
            
            while True:       
                try:
                    print("\nDeseja editar um novo produto?\n1. Sim\n2. Não")
                    escolha = int(input("\nDigite o numero: "))
                    if escolha == 2:
                        print("\n----------------")
                        print("Edição concluída.")
                        print("----------------\n")
                        return False
                    elif escolha == 1:
                        break
                    else:
                        raise ValueError("Valor inválido. Digite 1 ou 2.")
                except ValueError as erro_numero:
                    print(erro_numero)