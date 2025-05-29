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

def adicionar_produtos(conn, nome, quantidade, preco, id_usuario, id_categoria):
    cursor = None
    try:
        cursor = conn.cursor()
        query = "INSERT into PRODUTOS (nome, quantidade, valor_produto, id_usuario, id_categoria) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query,(nome, quantidade, preco, id_usuario, id_categoria))
        conn.commit()
        print(f"Produto: {nome} foi cadastrado no banco de dados com sucesso")
        return True
    except Exception as e:
        if conn:
            conn.rollback()
            print(f"Erro ao cadastrar produtos: {e}")
            return False
    finally:
        if cursor:
            cursor.close()

def mostrar_estoque(conn):
    cursor = None
    try:
        cursor = conn.cursor()
        query = "SELECT id_produto, nome, quantidade, valor_produto, id_usuario, id_categoria FROM PRODUTOS ORDER BY nome"
        cursor.execute(query)
        conn.commit()
        produtos = cursor.fetchall()
        return produtos
    except Exception as e:
        print(f"Erro ao mostrar o estoque: {e}")
        return []
    finally:
        if cursor:
            cursor.close

def excluir_produto(conn, exluir_id):
    cursor = None
    try:
        cursor = conn.cursor()
        query = "DELETE FROM produtos WHERE id_produto = %s"
        cursor.execute(query, (exluir_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("produto excluido com sucesso")
            return True
        else:
            print("Produto não encontrado")
            return False
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro ao tentar excluir o produto: {e}")
        return False
    finally:
        if cursor:
            cursor.close