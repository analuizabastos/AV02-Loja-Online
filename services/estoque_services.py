def adicionar_produtos(conn, nome, quantidade, preco, id_usuario, id_categoria):
    try:
        cursor = conn.cursor()
        query = "INSERT into PRODUTOS (nome, quantidade, valor_produto, id_usuario, id_categoria) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query,(nome, quantidade, preco, id_usuario, id_categoria))
        conn.commit()
        print(f"Produto: {nome} foi cadastrado com sucesso!")
        return True
    except Exception as e:
            conn.rollback()
            print(f"Erro ao cadastrar produtos: {e}")
            return False
    finally:
        if cursor:
            cursor.close()

def mostrar_estoque(conn):
    try:
        cursor = conn.cursor()
        query = "SELECT p.id_produto, p.nome, p.quantidade, p.valor_produto, c.nome FROM PRODUTOS p inner join CATEGORIA c on c.id_categoria = p.id_categoria ORDER BY p.nome"
        cursor.execute(query)
        produtos = cursor.fetchall()
        return produtos
    except Exception as e:
        print(f"Erro ao mostrar o estoque: {e}")
        return []
    finally:
        if cursor:
            cursor.close()

def excluir_produto(conn, excluir_id):
    try:
        cursor = conn.cursor()
        query = "DELETE FROM produtos WHERE id_produto = %s"
        cursor.execute(query, (excluir_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("produto excluido com sucesso")
            return True
        else:
            print("Produto não encontrado")
            return False
    except Exception as e:
        conn.rollback()
        print(f"Erro ao tentar excluir o produto: {e}")
        return False
    finally:
        if cursor:
            cursor.close

def editar_estoque(conn, id_editar, nome=None, quantidade=None, valor_produto=None, id_categoria=None):
    cursor = conn.cursor()
    try:
        campos = []
        valores = []

        
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
        
        query = f"UPDATE produtos SET {', '.join(campos)} WHERE id_produto = %s"
        valores.append(id_editar)
        cursor.execute(query, tuple(valores))
        conn.commit()

        if cursor.rowcount > 0:
            print("O produto foi atualizado com sucesso")
            return True
        else:
            print("o produto não foi editado")
            return False
    except Exception as e:
            conn.rollback()
            print(f"Erro ao editar o produto: {e}")
            return False
    finally:
        if cursor:
            cursor.close()
        