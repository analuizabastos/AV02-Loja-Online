def buscar_usuario(conn, nome_usuario):
    try:
        cursor = conn.cursor()
        query = "SELECT nome_usuario, senha, tipo FROM usuarios WHERE nome_usuario = %s"
        cursor.execute(query, (nome_usuario,))
        return cursor.fetchone()
    except Exception as e:
        print(f"Erro ao buscar usuário: {e}")
        return None
    
def cadastro_usuario(conn, nome, tipo, login, senha):
    try:
        cursor = conn.cursor()
        query = "INSERT into USUARIOS (nome, tipo, login, senha) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, [nome, tipo, login, senha])
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
        return None
