def validar_usuario(conn, id_final2):
    cursor = None
    try:
        cursor = conn.cursor()
        query = "SELECT 1 FROM usuarios WHERE id_usuario = %s"
        cursor.execute(query, (id_final2,))
        resultado = cursor.fetchone()

        return resultado is not None
    except Exception as e:
        print(f"Erro ao consultar a existencia do ususario {id_final2}: {e}")
        return False
    finally:
        if cursor:
            cursor.close()