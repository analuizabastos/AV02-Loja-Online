from Estoque.CadastroProduto import produtos
from Estoque.ExcluirProduto import RemoverProduto
from Estoque.EditarEstoque import editar

def menuEstoque():
    estoque = {}
    while True:
        print("----Estoque da Loja X----")
        print("\nO que deseja fazer?")
        print("\n1. Cadastrar produtos\n2. Ver estoque\n3. Excluir produto\n4. Editar estoque\n5. Sair\n")
        try:
            escolha2 = int(input("Digite um número: "))
            if escolha2 == 1:
                produtos(estoque)
            elif escolha2 == 2:
                if not estoque:
                    print("Estoque vazio.")
                    continue
                print("\n======================== PRODUTOS NO ESTOQUE ========================\n")
                for nome, info in estoque.items():
                    print(f"| Nome: {nome:<20}Preco: R${info['preco']:<10.2f}Quantidade: {info['quantidade']:<10}|\n")
                print("\n=====================================================================\n")
            elif escolha2 == 3:
                RemoverProduto(estoque)
            elif escolha2 == 4:
                editar(estoque)
            else:
                print("Sessão finalizada.")
                break
        except ValueError:
            print("Digite um valor válido.")