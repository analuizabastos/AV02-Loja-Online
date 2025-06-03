def inserir_log(conn, id_usuario, tipo_acao, descricao, sucesso):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO logs (id_usuario, tipo_acao, descricao, sucesso) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (id_usuario, tipo_acao, descricao, sucesso))
        conn.commit()
    except Exception as e:
        print(f"Erro ao inserir log: {e}")
    finally:
        cursor.close()

