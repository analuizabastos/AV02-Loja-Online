def buscar_usuario(conn, login):
    try:
        cursor = conn.cursor()
        query = "SELECT nome, tipo, login, senha FROM usuarios WHERE login = %s"
        cursor.execute(query, (login,))
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
