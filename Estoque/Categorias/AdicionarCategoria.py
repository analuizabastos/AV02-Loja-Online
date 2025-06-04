from Estoque.Categorias.MostrarCategorias import Exibir_categorias
from Validacoes.ValidacaoNome import validar_nome
from services.estoque_services import adicionar_categorias

def Adicao_de_categorias(conn):
    while True:
        while True:
            print("\nDigite -Sair- para voltar para o Menu.")
            nome = input("\nNome da nova categoria: ").upper()
            try:
                if nome == "SAIR":
                    return
                validar_nome(nome)
                nova_categoria = nome
                break
            except ValueError as erro:
                print(erro)
        while True:
            try:
                print("Deseja cadastrar essa categoria?\n1. Sim\n2. Não")
                print(nova_categoria)
                resposta = int(input("Digite um numero: "))
                if resposta == 1:
                    sucesso = adicionar_categorias(conn, nome=nova_categoria)
                    if sucesso:
                        print("categoria cadastrada com sucesso")
                        break
                    else:
                        print("Erro ao cadastrar a nova categoria.")
                        break
                elif resposta == 2:
                    print("Cadastro cancelado.")
                    break
                else:
                    raise ValueError("Valor inválido. Digite 1 ou 2.")
            except ValueError as erro_numero:
                print(erro_numero)

    