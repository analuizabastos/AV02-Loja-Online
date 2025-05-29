from Estoque.Mostrarestoque import exibir_estoque
from services.user_services import editar_estoque
from Validacoes.ValidarIdProduto import validar_idproduto

def editar(conn):
    while True:
        exibir_estoque(conn)
        novo_nome = None
        nova_quantidade = None
        novo_valor = None
        nova_categoria = None
        while True:
            print("Digite -Sair- para voltar para o Menu.\n")
            try:
                numero = input("Informe o id do produto que deseja editar: ").strip()
                if numero.upper() == "SAIR":
                    return
                resposta = int(numero)
                if validar_idproduto(conn, resposta):
                    id_produto = resposta
                    print("Id validado com sucesso")
                    break
                else:
                    print("Id invalido")
            except ValueError:
                print("Digite um numero válido")
        while True:
            print("=" * 50)
            print("Lista das partes que podem ser editadas")
            print("=" * 50)
            print("1 - Nome\n2 - Quantidade\n3 - Valor\n4 - Categoria\n 0 - Concluir\nDigite -Sair- para voltar para o Menu.")
            try:
                campo = input("Digite um número: ").strip()
                if campo.upper() == "SAIR":
                    return
                if campo == 0:
                    break
                elif campo == 1:
                    novo_nome = input("Informe o novo nome para o produto: ").strip()
                elif campo == 2:
                    nova_quantidade0 = input("Informe a nova quantidade: ")
                    nova_quantidade = int(nova_quantidade0)
                elif campo == 3:
                    novo_valor0 = input("Informe o novo valor: ")
                    novo_valor = float(novo_valor0)
                else:
                    print("---------- CATEGORIAS -----------\n")
                    print("1 - Eletronicos\n")
                    print("2 - Livros\n")
                    print("3 - Roupas\n")
                    nova_categoria0 = input("Digite um numero")
                    nova_categoria = int(nova_categoria0)
            except ValueError:
                print("Numero invalido")
        while True:
            try:
                print("Deseja salvar essa alterações? 1 - Sim 2 - Não")
                opcao = int(input("Digite um numero"))
                if opcao == 1:
                    sucesso = editar_estoque(conn, id_produto, nome=novo_nome, quantidade=nova_quantidade, valor_produto=novo_valor, id_categoria=nova_categoria)
                    if sucesso:
                        print("Produto editado com sucesso")
                        break
                    else:
                        print("Erro ao editar produto")
                elif opcao == 2:
                    print("Edição cancelada")
                    break
            except ValueError:
                print("Numero invalido")
        
        while True:       
            try:
                print("\nDeseja editar um novo produto?\n1. Sim\n2. Não")
                escolha = int(input("\nDigite o numero: "))
                if escolha == 2:
                    print("\n----------------")
                    print("Edição conlcuida.")
                    print("----------------\n")
                    return False
                elif escolha == 1:
                    break
                else:
                    raise ValueError("Valor inválido. Digite 1 ou 2.")
            except ValueError as erro_numero:
                print(erro_numero)