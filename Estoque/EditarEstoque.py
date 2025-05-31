from Estoque.Mostrarestoque import exibir_estoque
from services.estoque_services import editar_estoque
from Validacoes.ValidarIdProduto import validar_idproduto
from Validacoes.ValidacaoNome import validar_nome
from Validacoes.ValidacaoPreco import validar_preco
from Validacoes.ValidacaoQuantidade import validar_quantidade

def editar(conn, acesso):
    while True:
        exibir_estoque(conn)
        novo_nome = None
        nova_quantidade = None
        novo_preco = None
        nova_categoria = None
        while True:
            print("Digite -Sair- para voltar para o Menu.\n")
            try:
                numero = input("Informe o id do produto que deseja editar: ").strip()
                if numero.upper() == "SAIR":
                    return
                produto = int(numero)
                if validar_idproduto(conn, produto):
                    id_produto = produto
                    break
                else:
                    print("Id inválido. Tente Novamente.")
                    continue
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
                                nova_quantidade = int(quantidade)
                                validar_quantidade(nova_quantidade)
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
                    print("Deseja salvar essa alterações? 1 - Sim 2 - Não")
                    opcao = int(input("Digite um numero"))
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