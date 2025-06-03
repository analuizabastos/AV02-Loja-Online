def lista_de_pedidos(conn):
    try:
        cursor = conn.cursor()
        query = "SELECT p.id_pedido, p.data_pedido, p.valor_total, p.forma_pagamento, c.nome FROM pedido p INNER JOIN clientes c on p.id_cliente = c.id_cliente ORDER BY p.data_pedido DESC"
        cursor.execute(query)
        pedidos = cursor.fetchall()
        return pedidos
    except Exception as e:
        print(f"Erro ao listar pedidos: {e}")
        return []
    finally:
        cursor.close()