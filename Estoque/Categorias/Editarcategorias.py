from services.estoque_services import alterar_categorias
from Estoque.Categorias.MostrarCategorias import mostrar_categorias
from Validacoes.ValidarIdCategoria import validar_idcategoria
from Validacoes.ValidacaoNome import validar_nome
from Estoque.Categorias.ExcluirCategoria import excluir_categoria
from services.logs_services import inserir_log

def editar_categorias(conn, id_usuario):
    mostrar_categorias(conn)
    while True:
        print("Digite -Sair- para voltar para o Menu.\n")
        try:
            numero = input("Informe o id da categoria: ").strip()
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
        print("\n1. Editar categoria\n2. Excluir categoria")
        print("Digite -Sair- para voltar para o Menu.\n")
        resposta = input("Digite um numero: ")
        try:
            if resposta.upper() == "SAIR":
                return
            resposta = int(resposta)
            if resposta == 2:
                excluir_categoria(conn, id_categoria, id_usuario)
                break
            elif resposta == 1:
                while True:
                    nome = input("Informe o novo nome para a categoria: ").upper()
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
                                print("Categoria editada com sucesso!")
                                inserir_log(conn, id_usuario, "EDITAR_CATEGORIA_SUCESSO", f"Nome da Categoria de ID: '{id_categoria}' alterado.", True)
                                return
                            else:
                                print("Erro ao editar categoria.")
                                inserir_log(conn, id_usuario, "EDITAR_CATEGORIA_SUCESSO", f"Falha ao alterar a Categoria de ID: '{id_categoria}'.", False)
                        elif opcao == 2:
                            print("Edição cancelada.")
                            break
                    except ValueError:
                        print("Valor inválido.")
        except ValueError:
            print("Valor inválido.")
