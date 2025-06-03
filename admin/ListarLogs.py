from services.log_services import lista_de_logs

def listar_logs(conn):
    print("-" * 150)
    print("                                LOGS DE ATIVIDADE")
    print("-" * 150)
    logs = lista_de_logs(conn)

    if logs:
        print(f"\n{'ID Log':<10} {'ID Usuário':<12} {'AÇÃO':<15} {'DESCRIÇÃO':<50} {'DATA/HORA':<30} {'SUCESSO':<8}")
        print("-" * 150)

        for id_log, id_usuario, tipo_acao, descricao, data_hora, sucesso in logs:
            status_sucesso = "Sim" if sucesso else "Não"
            print(f"{id_log:<10} {id_usuario:<12} {tipo_acao:<15} {descricao:<50} {str(data_hora):<30} {status_sucesso:<8}")
    else:
        print("Nenhum log encontrado no sistema.")
        print("-" * 100)