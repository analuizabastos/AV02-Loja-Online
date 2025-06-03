from services.estoque_services import alterar_categorias
from Estoque.MostrarCategorias import Exibir_categorias
from Validacoes.ValidarIdCategoria import validar_idcategoria
from Validacoes.ValidacaoNome import validar_nome

def editar_categorias(conn):
    Exibir_categorias(conn)
    while True:
        while True:
            print("Digite -Sair- para voltar para o Menu.\n")
            try:
                numero = input("Informe o id da categoria que deseja editar: ").strip()
                if numero.upper() == "SAIR":
                    return
                id_categoria = int(numero)
                if validar_idcategoria(conn, id_categoria):
                    break
                else:
                    print("Id inválido. Tente Novamente.")
                    continue
            except ValueError:
                print("Digite um numero válido")
        while True:
            nome = input("Informe o novo nome para o produto: ").upper()
            try:
                validar_nome(nome)
                novo_nome = nome
                break 
            except ValueError as erro:
                print(erro)
        while True:
            try:
                print("Deseja salvar essa alterações? \n1 - Sim \n2 - Não")
                opcao = int(input("Digite um número: "))
                if opcao == 1:
                    sucesso = alterar_categorias(conn, id_categoria, novo_nome)
                    if sucesso:
                        print("Produto editado com sucesso!")
                        break
                    else:
                        print("Erro ao editar produto.")
                elif opcao == 2:
                    print("Edição cancelada.")
                    break
            except ValueError:
                print("Valor inválido.")