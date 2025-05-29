from services.user_services import mostrar_estoque

def exibir_estoque(conn):
    print("=" * 100)
    print("                                ESTOQUE DE PRODUTOS")
    print("=" * 100)

    exibir_estoque = mostrar_estoque(conn)

    if exibir_estoque:
        print(f"{'ID':<5} {'NOME':<20} {'QUANTIDADE':<12} {'VALOR':<15} {'ID_USUARIO':<12} {'ID_CATEGORIA':<15}")
        print("-" * 100)
        for produtos in exibir_estoque:
            id_produto, nome, quantidade, valor_produto, id_usuario, id_categoria = produtos
            print(f"{id_produto:<5} {nome:<20} {quantidade:<12} R${valor_produto:<11.2f} {id_usuario:<12} {id_categoria:<15}")
            print("-" * 100)
    else:
        print("Nenhum produto dentro do estoque")
