from services.pedido_services import lista_de_pedidos
def listar_pedidos(conn):
    print("-" * 100)
    print("                                Pedidos")
    print("-" * 100)

    pedidos = lista_de_pedidos(conn)
    if pedidos:
        print(f"\n{'ID':<5} {'DATA':<20} {'VALOR':<10} {'FORMA DE PAGAMENTO':<20} {'CLIENTE':<20}")
        print("-" * 100)
        for id_pedido, data_pedido, valor_total, forma_pagamento, id_cliente in pedidos:
            data_str = str(data_pedido)
            print(f"{id_pedido:<5} {data_str:<20} {valor_total:<10} {forma_pagamento:<20} {id_cliente:<8}")
    else:
        print("Nenhum pedido encontrado.")