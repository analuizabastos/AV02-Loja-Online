from Estoque.CadastroProduto import produtos
from Estoque.ExcluirProduto import remover_Produto
from Estoque.EditarEstoque import editar
from Estoque.Mostrarestoque import exibir_estoque

def menuEstoque(conn):
    while True:
        print("\n----Estoque da Loja X----")
        print("\nO que deseja fazer?")
        print("\n1. Cadastrar produtos\n2. Ver estoque\n3. Excluir produto\n4. Editar estoque\n5. Sair\n")
        try:
            escolha2 = int(input("Digite um número: "))
            if escolha2 in [1,2,3,4,5]:
                if escolha2 == 1:
                    produtos(conn)
                elif escolha2 == 2:
                    exibir_estoque(conn)
                elif escolha2 == 3:
                    remover_Produto(conn)
                elif escolha2 == 4:
                    print("Erro")
                else:
                    print("Sessão finalizada.")
                    break
            else:
                print("Valor inválido. Digite um valor do menu.")
        except ValueError:
            print("Digite um valor válido.")