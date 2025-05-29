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
    
def editar_usuario(conn, login_atual, nome=None, tipo=None, novo_login=None, senha=None):
    try:
        cursor = conn.cursor()
        campos = []
        valores = []
        if nome:
            campos.append("nome = %s")
            valores.append(nome)
        if tipo:
            campos.append("tipo = %s")
            valores.append(tipo)
        if novo_login:
            campos.append("login = %s")
            valores.append(novo_login)
        if senha:
            campos.append("senha = %s")
            valores.append(senha)
        if not campos:
            print("Nenhuma alteração foi feita.")
            return False

        query = f"UPDATE usuarios SET {', '.join(campos)} WHERE login = %s"
        valores.append(login_atual)

        cursor.execute(query, valores)
        conn.commit()
        return True

    except Exception as e:
        print(f"Erro ao editar usuário: {e}")
        return False

def excluir_usuario(conn, login):
    try:
        cursor = conn.cursor()
        query = "DELETE from USUARIOS WHERE login = %s"
        cursor.execute(query, (login,))
        conn.commit()
        if cursor.rowcount == 0:
            print("Nenhum usuário foi excluído.")
            return False
        return True
    except Exception as e:
        print(f"Erro ao excluir usuário: {e}")
        return None