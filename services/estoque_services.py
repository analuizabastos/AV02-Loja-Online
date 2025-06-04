def adicionar_produtos_bd(conn, nome, quantidade, preco, id_usuario, id_categoria):
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

def buscar_produto(conn, termo_busca):
    try:
        cursor = conn.cursor()
        termo_formatado = f"%{termo_busca.upper()}%"
        query = "SELECT id_produto, nome, quantidade, valor_produto FROM produtos WHERE upper(nome) LIKE %s"
        cursor.execute(query, (termo_formatado,))
        resultados = cursor.fetchall() 
        return resultados
    except Exception as e:
        print(f"Erro ao buscar produto: {e}")
        return []
    finally:
        cursor.close()

def buscar_produto_id(conn, id_produto):
    try:
        cursor = conn.cursor()
        query = "SELECT id_produto, nome, quantidade, valor_produto, id_usuario, id_categoria FROM produtos WHERE id_produto = %s"
        cursor.execute(query, (id_produto,))
        return cursor.fetchone()
    except Exception as e:
        print(f"Erro ao buscar produto por ID exato: {e}")
        return None
    finally:
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
            print("Produto excluído com sucesso!")
            return True
        else:
            print("Produto não encontrado.")
            return False
    except Exception as e:
        conn.rollback()
        print(f"Erro ao tentar excluir o produto: {e}")
        return False
    finally:
        if cursor:
            cursor.close()

def editar_estoque_bd(conn, id_editar, nome=None, quantidade=None, valor_produto=None, id_categoria=None):
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


def Exibir_categorias(conn):
    try:
        cursor = conn.cursor()
        query = "SELECT id_categoria, nome FROM categoria"
        cursor.execute(query)
        categorias = cursor.fetchall()
        return categorias
    except Exception as e:
        print(f"Erro ao mostrar o categorias: {e}")
        return []
    finally:
        if cursor:
            cursor.close()


def adicionar_categorias(conn, nome):
    cursor = None
    try:
        cursor = conn.cursor()
        query = "INSERT INTO categoria (nome) VALUES (%s)"
        cursor.execute(query, (nome,))
        conn.commit()
        print(f"Categoria: {nome} foi adicionada com sucesso!")
        return True
    except Exception as e:
        conn.rollback()
        print(f"Erro ao tentar cadastrar categorias: {e}")
        return False
    finally:
        if cursor:
            cursor.close()

    
def alterar_categorias(conn, id_categoria, novo_nome=None):
    cursor = None
    try:
        cursor = conn.cursor()
        campos = []
        valores = []

        if novo_nome is not None:
            campos.append("nome = %s")
            valores.append(novo_nome)
        
        if not campos:
            print("Nenhum campo para editar foi fornecido.")
            return False

        query = f"UPDATE categoria SET {', '.join(campos)} WHERE id_categoria = %s"
        valores.append(id_categoria)
        cursor.execute(query, tuple(valores))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"A categoria de ID {id_categoria} foi atualizada com sucesso!")
            return True
        else:
            print(f"Nenhuma categoria encontrada com o ID ou nenhum dado alterado.")
            return False
            
    except Exception as e:
        conn.rollback()
        print(f"Erro ao editar a categoria: {e}")
        return False
    finally:
        if cursor:
            cursor.close()


def excluir_categoria_bd(conn, excluir_id):
    try:
        cursor = conn.cursor()
        query = "DELETE FROM categoria WHERE id_categoria = %s"
        cursor.execute(query, (excluir_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Categoria excluída com sucesso!")
            return True
        else:
            print("Categoria não encontrado.")
            return False
    except Exception as e:
        conn.rollback()
        print(f"Erro ao tentar excluir o Categoria: {e}")
        return False
    finally:
        if cursor:
            cursor.close()