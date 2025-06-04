from Estoque.Mostrarestoque import exibir_estoque
from services.estoque_services import excluir_produto

def remover_Produto(conn): 

    exibir_estoque(conn)
    while True:
        try:   
            print("Digite -Sair- para voltar para o Menu.\n")
            numero = input("Informe o id do produto que deseja excluir: ").strip()
            if numero.upper() == "SAIR":
                return
            excluir_id = int(numero)
            excluir_produto(conn, excluir_id)
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
