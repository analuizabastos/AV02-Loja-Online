from services.logs_services import lista_de_logs_totais, lista_de_logs_usuario

def listar_logs(conn):
    while True:    
        print("\nO que gostaria de ver?")
        print("1.Listar todas as Logs")
        print("2.Listar as logs de um usuário específico")
        print("Digite -Sair- para voltar para o Menu Administrativo.\n")
        escolha = input("Digite um número: ")
        while True:
            if escolha in ["1","2"]:
                if escolha == "1":
                    print("-" * 150)
                    print("                                LOGS DE ATIVIDADE")
                    print("-" * 150)
                    logs = lista_de_logs_totais(conn, None)

                    if logs:
                        print(f"\n{'ID Log':<10} {'ID Usuário':<12} {'AÇÃO':<30} {'DESCRIÇÃO':<50} {'DATA/HORA':<30} {'SUCESSO':<8}")
                        print("-" * 150)

                        for id_log, id_usuario, tipo_acao, descricao, data_hora, sucesso in logs:
                            status_sucesso = "Sim" if sucesso else "Não"
                            print(f"{id_log:<10} {id_usuario:<12} {tipo_acao:<30} {descricao:<50} {str(data_hora):<30} {status_sucesso:<8}")
                    else:
                        print("-" * 100)
                        print("Nenhum log encontrado no sistema.")
                        print("-" * 100)
                    break
                elif escolha == "2":
                    id_usuario = input("Digite o ID do usuário que deseja ver as atividades: ")
                    logs = lista_de_logs_usuario(conn, id_usuario)
                    if logs:
                        print(f"\n{'ID Log':<10} {'ID Usuário':<12} {'AÇÃO':<30} {'DESCRIÇÃO':<50} {'DATA/HORA':<30} {'SUCESSO':<8}")
                        print("-" * 150)

                        for id_log, id_usuario, tipo_acao, descricao, data_hora, sucesso in logs:
                            status_sucesso = "Sim" if sucesso else "Não"
                            print(f"{id_log:<10} {id_usuario:<12} {tipo_acao:<30} {descricao:<50} {str(data_hora):<30} {status_sucesso:<8}")
                    else:
                        print("-" * 100)
                        print("Nenhum log encontrado no sistema.")
                        print("-" * 100)
                    break
            elif escolha.upper() == "SAIR":
                    return
            else:
                print("Opção inválida.")
                break
