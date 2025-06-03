from services.estoque_services import Exibir_categorias
def mostrar_categorias(conn):
    print("-" * 50)
    print("                    CATEGORIAS")
    print("-" * 50)

    lista_categorias = Exibir_categorias(conn)

    if lista_categorias:
        print(f"{'ID':<5} {'NOME':<10}")
        print("-" * 50)
        for categorias in lista_categorias:
            id_categorias, nome = categorias
            print(f"{id_categorias:<5} {nome:<10}")
            print("-" * 50)
    else:
        print("Nenhuma categoria dentro do sistema.")