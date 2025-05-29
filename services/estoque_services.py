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

def editar_estoque(conn, id_editar, nome=None, quantidade=None, valor_produto=None, id_categoria=None):
    cursor = None
    try:
        campos = []
        valores = []
        cursor = conn.cursor()
        if nome is not None:
            campos.append("nome = %s")
            valores.append(nome)
        if quantidade is not None:
            campos.append("quantidade = %s")
            valores.append(quantidade)
        if valor_produto is not None:
            campos.append("valor_produto = %s")
            valores.append(valor_produto)
        if id_categoria is not None:
            campos.append("id_categoria = %s")
            valores.append(id_categoria)
        
        valor = ", ".join(campos)

        valores.append(id_editar)

        query = f"UPDATE produtos SET {valor} WHERE id_produto = %s;"
        cursor.execute(query, tuple(valores))
        conn.commit()

        if cursor.rowcount > 0:
            print("O produto foi atualizado com sucesso")
            return True
        else:
            print("o produto não foi editado")
            return False
    except Exception as e:
        if conn:
            conn.rollback()
            print(f"Erro ao editar o produto: {e}")
            return False
    finally:
        if cursor:
            cursor.close()
        