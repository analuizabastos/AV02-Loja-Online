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

def lista_de_logs(conn):
    try:
        cursor = conn.cursor()
        query = "SELECT id_log, id_usuario, tipo_acao, descricao, data_hora, sucesso FROM logs ORDER BY data_hora DESC"
        cursor.execute(query)
        logs = cursor.fetchall()
        return logs
    except Exception as e:
        print(f"Erro ao listar logs: {e}")
        return []
    finally:
        cursor.close()

