def validar_idcategoria(conn, id_categoria):
    cursor = None
    try:
        cursor = conn.cursor()
        query = "SELECT COUNT 1 FROM categorias WHERE id_categoria = %s"
        cursor.execute(query, (id_categoria,))
        count = cursor.fetchone()[0]
        return count > 0
    except Exception as e:
        print(f"Erro na validação do ID:{id_categoria}: {e}")
        return False
    finally:
        if cursor:
            cursor.close()