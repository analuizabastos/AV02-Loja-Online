from Estoque.MostrarCategorias import Exibir_categorias
from services.estoque_services import excluir_categoria_bd
def excluir_categoria(conn, excluir_id):
    Exibir_categorias(conn)
    while True:
        try:   
            excluir_categoria_bd(conn, excluir_id)
        except ValueError as erro:
            print(erro)
        while True:
            try:
                print("\nDeseja remover mais alguma categoria?\n1. Sim\n2. Não")
                numero = int(input("\nDigite um numero: "))
                if numero == 1:  
                    break
                elif numero == 2:
                    print("Encerrando...")
                    return
                else:
                    print("Numero inválido, digite 1 ou 2")
            except ValueError:
                print("Resposta inválida, digite apenas 1 ou 2")

