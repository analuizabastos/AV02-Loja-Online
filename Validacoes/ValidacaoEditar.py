from Validacoes.ValidacaoNome import validar_nome
from Validacoes.ValidacaoPreco import validar_preco
from Validacoes.ValidacaoQuantidade import validar_quantidade

def validacao(estoque, nome, escolha):
    if escolha == 1:
        while True:
            try:
                novo_nome = input("Digite um novo nome: ").upper().strip()
                validar_nome(novo_nome)
                if novo_nome not in estoque:
                    estoque[novo_nome] = estoque.pop(nome)
                    break
                else:
                    raise ValueError("Produto já existe. Digite um novo nome.")
            except ValueError as erro:
                print(erro)
    elif escolha == 2:
            while True:
                try: 
                    novo_preco = float(input("Digite o novo preço: "))
                    validar_preco(novo_preco)
                    estoque[nome]['preco'] = novo_preco
                    break
                except ValueError:
                    print("Preco inválido. Digite apenas números.")
    elif escolha == 3:
        while True:
            try:
                nova_quantidade = input("Digite a nova quantidade: ")
                validar_quantidade(nova_quantidade)
                estoque[nome]['quantidade'] = nova_quantidade
                break
            except ValueError as erro:
                   print(erro)