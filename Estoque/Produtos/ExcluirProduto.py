from Estoque.Produtos.MostrarEstoque import exibir_estoque
from services.estoque_services import excluir_produto
from services.logs_services import inserir_log

def remover_Produto(conn, id_usuario): 
    exibir_estoque(conn)
    while True:
        try:   
            print("Digite -Sair- para voltar para o Menu.\n")
            numero = input("Informe o id do produto que deseja excluir: ").strip()
            if numero.upper() == "SAIR":
                inserir_log(conn, id_usuario, "EXCLUSAO_PRODUTO_CANCELADA", f"Exclusão do produto (ID: {excluir_id}) cancelada por escolha do usuário.", False)
                return
            excluir_id = int(numero)
            excluir_produto(conn, excluir_id)
            inserir_log(conn, id_usuario, "EXCLUSAO_PRODUTO_SUCESSO", f"Produto (ID: '{excluir_id}') excluído com sucesso.", True)
            print(f"Produto ID {excluir_id} excluído com sucesso.")
        except ValueError as erro:
            print(erro)
        while True:
            try:
                print("\nDeseja remover mais algum item?\n1. Sim\n2. Não")
                numero = int(input("\nDigite um numero: "))
                if numero == 1:  
                    break
                elif numero == 2:
                    print("Encerrando...")
                    return
                else:
                    print("Numero inválido, digite 1 ou 2")
            except ValueError:
                print("Resposta inválida, digite apenas 1 ou 2")
