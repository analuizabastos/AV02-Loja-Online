import psycopg2

def criar_conexao():
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",  # Ou o endereço do seu servidor PostgreSQL
            database="postgres",
            user="postgres",
            password="post"
        )
        print("Conexão com o PostgreSQL estabelecida com sucesso!")
        return conn
    except erro as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None
