def buscar_usuario(conn, nome_usuario):
    try:
        cursor = conn.cursor()
        query = "SELECT nome_usuario, senha, tipo FROM usuarios WHERE nome_usuario = %s"
        cursor.execute(query, (nome_usuario,))
        return cursor.fetchone()
    except Exception as e:
        print(f"Erro ao buscar usuário: {e}")
        return None
