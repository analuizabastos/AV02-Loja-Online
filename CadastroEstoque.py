def produtos(estoque):
    while True:
        while True:
            try:
                nome = input("Nome do produto: ")
                for caractere in nome:
                    if not caractere.isalpha():
                        raise ValueError("Nome inválido. Use apenas letras.")
                break 
            except ValueError as erro:
                print(erro)
        
        while True:    
            try:    
                preco = float(input("Preço do produto: "))
                if preco < 0:
                    raise ValueError("Preco Invalido. Deve ser positivo.") 
                break
            except ValueError:
                print("Preco invalido. Digite apenas numeros.")   
        
        while True:
            try:
                quantidade = (input("Quantidade do produto: ")).strip()
                for caractere in quantidade:
                    if not caractere.isnumeric():
                        raise ValueError("Quantidade invalida. Digite apenas numeros inteiros.")
                quantidade = int(quantidade)
                if quantidade < 0:
                    print("Quantidade invalida. Deve ser positivo.")
                    continue
                break
            except ValueError as erro:
                print(erro)
                
            estoque[nome] = {
                'preco': preco,
                'quantidade': quantidade
            }
        break
    
    while True:       
        try:
            print("Deseja cadastrar um novo produto?\n1. Sim\n2. Não")
            escolha = int(input("Digite o numero: "))
            if escolha == 2:
                print("Cadastro de produtos concluido.")
                return False
            if escolha == 1:
                break
            else:
                raise ValueError("Valor inválido. Digite 1 ou 2.")
        except ValueError as erro_numero:
            print(erro_numero)