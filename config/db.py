import psycopg2

def criar_conexao():
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost", 
            database="postgres",
            user="postgres",
            password="post"
        )
        cursor = conn.cursor()
        cursor.execute("SET search_path TO lojaonline;")
        conn.commit()
        print("Conexão com o PostgreSQL estabelecida com sucesso!")
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None
