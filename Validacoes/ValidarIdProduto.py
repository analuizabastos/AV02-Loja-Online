def validar_idproduto (conn, resposta):
    cursor = None
    try:
        cursor = conn.cursor()
        query = "SELECT 1 FROM produtos WHERE id_produto = %s"
        cursor.execute(query(resposta, ))
        resultado = cursor.fetchone()
        
        return resultado is not None
    except Exception as e:
        conn
        print(f"Erro ao consultar {resposta}: {e}")
        return False
    finally:
        if cursor:
            cursor.close()