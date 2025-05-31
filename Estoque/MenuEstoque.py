from Estoque.CadastroProduto import cadastro_produto
from Estoque.ExcluirProduto import remover_Produto
from Estoque.EditarEstoque import editar
from Estoque.Mostrarestoque import exibir_estoque

def menuEstoque(conn, acesso):
    while True:
        print("\n----Estoque da Loja X----")
        print("\nO que deseja fazer?")
        print("\n1. Cadastrar produtos\n2. Ver estoque\n3. Excluir produto\n4. Editar estoque\n5. Sair\n")
        try:
            escolha = int(input("Digite um número: "))
            if escolha in [1,2,3,4,5]:
                if escolha == 1:
                    cadastro_produto(conn, acesso["id"])
                elif escolha == 2:
                    exibir_estoque(conn)
                elif escolha == 3:
                    remover_Produto(conn)
                elif escolha == 4:
                    editar(conn, acesso["id"])
                else:
                    print("Sessão finalizada.")
                    break
            else:
                print("Valor inválido. Digite um valor do menu.")
        except ValueError:
            print("Digite um valor válido.")