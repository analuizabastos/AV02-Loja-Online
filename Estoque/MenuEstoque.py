from Estoque.Produtos.CadastroProduto import cadastro_produto
from Estoque.Produtos.ExcluirProduto import remover_Produto
from Estoque.Produtos.EditarProduto import editar_produto
from Estoque.Produtos.MostrarEstoque import exibir_estoque
from Estoque.Categorias.AdicionarCategoria import Adicao_de_categorias
from Estoque.Categorias.Editarcategorias import editar_categorias

def menuEstoque(conn, id_usuario):
    while True:
        print("\n----Estoque da Loja X----")
        print("\nO que deseja fazer?")
        print("\n1. Cadastrar produtos\n2. Ver estoque\n3. Excluir produto\n4. Editar estoque\n5. Adicionar categorias\n6. Editar categorias\n7. . Sair\n")
        try:
            escolha = int(input("Digite um número: "))
            if escolha in [1,2,3,4,5,6,7]:
                if escolha == 1:
                    cadastro_produto(conn, id_usuario)
                elif escolha == 2:
                    exibir_estoque(conn)
                elif escolha == 3:
                    remover_Produto(conn)
                elif escolha == 4:
                    editar_produto(conn)
                elif escolha == 5:
                    Adicao_de_categorias(conn)
                elif escolha == 6:
                    editar_categorias(conn)
                else:
                    print("Sessão finalizada.")
                    break
            else:
                print("Valor inválido. Digite um valor do menu.")
        except ValueError:
            print("Digite um valor válido.")