def validar_quantidade(quantidade):
    for caractere in quantidade:
        if not caractere.isnumeric():
            raise ValueError("Quantidade invalida. Digite apenas numeros inteiros.")
    if not quantidade:
        raise ValueError("Nome inválido. O nome não pode ser espaços vazios.")
    quantidade = int(quantidade)
    if quantidade < 0:
        raise ValueError("Quantidade invalida. Deve ser positivo.")