def validar_preco(preco):
    if preco < 0:
        raise ValueError("Preco Invalido. Deve ser positivo.") 