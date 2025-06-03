def validar_idproduto (conn, id_produto):
    cursor = None
    try:
        cursor = conn.cursor()
        query = "SELECT COUNT 1 FROM produtos WHERE id_produto = %s"
        cursor.execute(query, (id_produto,))
        count = cursor.fetchone()[0]
        return count > 0
    except Exception as e:
        print(f"Erro ao consultar {id_produto}: {e}")
        return False
    finally:
        if cursor:
            cursor.close()