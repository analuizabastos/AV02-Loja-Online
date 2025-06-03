import bcrypt, base64

def criar_usuario_master(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM usuarios WHERE login = 'MASTER'")
    if cursor.fetchone():
        cursor.close()
    else:
        nome = 'MASTER'
        tipo = 'MASTER'
        login = 'MASTER'
        senha_codificada = "c2VuaGFNYXN0ZXIxMjM=" 
        senha_plana = base64.b64decode(senha_codificada.encode()).decode()
        senha_hash = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


        cursor.execute("""
            INSERT INTO usuarios (nome, tipo, login, senha)
            VALUES (%s, %s, %s, %s)
        """, (nome, tipo, login, senha_hash))

        conn.commit()
        print("Usuário master criado com sucesso!")
        cursor.close()