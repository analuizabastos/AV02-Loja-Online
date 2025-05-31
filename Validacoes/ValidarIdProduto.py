def validar_idproduto (conn, id_produto):
    cursor = None
    try:
        cursor = conn.cursor()
        query = "SELECT 1 FROM produtos WHERE id_produto = %s"
        cursor.execute(query(id_produto, ))
        resultado = cursor.fetchone()
        
        return resultado is not None
    except Exception as e:
        conn
        print(f"Erro ao consultar {id_produto}: {e}")
        return False
    finally:
        if cursor:
            cursor.close()