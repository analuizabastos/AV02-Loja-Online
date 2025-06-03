import bcrypt

def criptografar(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    hashed_string = hashed_bytes.decode('utf-8')
    return hashed_string