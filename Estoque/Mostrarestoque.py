from services.user_services import mostrar_estoque

def exibir_estoque(conn):
    print("===============================================")
    print("             ESTOQUE DE PRODUTOS                 ")
    print("===============================================\n")

    exibir_estoque = mostrar_estoque(conn)

    if exibir_estoque:
        print(f"{'ID':<5} {'NOME':<30} {'QUANTIDADE':<12} {'VALOR':<10} {'ID_USUARIO':<8} {'ID_CATEGORIA':<8}")
        print("-" * 100)
        for produtos in exibir_estoque:
            id_produto, nome, quantidade, valor_produto, id_usuario, id_categoria = produtos
            print(f"{id_produto:<5} {nome:<30} {quantidade:<8} R${valor_produto:<12} {id_usuario:<10} {id_categoria:<13}")
            print("-" * 100)
    else:
        print("Nenhum produto dentro do estoque")
