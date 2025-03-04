### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. Dado um registro de log em formato de dicionário como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

logs = [
    {'timestamp': '2024-03-04 08:15:00', 'level': 'INFO', 'message': 'Sistema iniciado'},
    {'timestamp': '2024-03-04 08:16:00', 'level': 'WARNING', 'message': 'Uso elevado de memória'},
    {'timestamp': '2024-03-04 08:17:00', 'level': 'ERROR', 'message': 'Falha ao conectar ao banco de dados'},
    {'timestamp': '2024-03-04 08:18:00', 'level': 'DEBUG', 'message': 'Verificando conexões ativas'},
    {'timestamp': '2024-03-04 08:19:00', 'level': 'ERROR', 'message': 'Arquivo de configuração não encontrado'},
    {'timestamp': '2024-03-04 08:20:00', 'level': 'INFO', 'message': 'Usuário logado com sucesso'},
    {'timestamp': '2024-03-04 08:21:00', 'level': 'ERROR', 'message': 'Tempo limite de requisição excedido'},
    {'timestamp': '2024-03-04 08:22:00', 'level': 'WARNING', 'message': 'Espaço em disco baixo'},
    {'timestamp': '2024-03-04 08:23:00', 'level': 'DEBUG', 'message': 'Execução de tarefa agendada iniciada'},
    {'timestamp': '2024-03-04 08:24:00', 'level': 'ERROR', 'message': 'Falha na autenticação do usuário'},
    {'timestamp': '2024-03-04 08:25:00', 'level': 'INFO', 'message': 'Backup concluído com sucesso'},
    {'timestamp': '2024-03-04 08:26:00', 'level': 'WARNING', 'message': 'Latência da rede elevada'},
    {'timestamp': '2024-03-04 08:27:00', 'level': 'ERROR', 'message': 'Serviço de e-mail não disponível'},
    {'timestamp': '2024-03-04 08:28:00', 'level': 'DEBUG', 'message': 'Processo de limpeza de cache iniciado'},
    {'timestamp': '2024-03-04 08:29:00', 'level': 'ERROR', 'message': 'Falha ao acessar o servidor de arquivos'},
    {'timestamp': '2024-03-04 08:30:00', 'level': 'INFO', 'message': 'Atualização do sistema concluída'},
    {'timestamp': '2024-03-04 08:31:00', 'level': 'ERROR', 'message': 'Erro de permissão ao acessar diretório'},
    {'timestamp': '2024-03-04 08:32:00', 'level': 'WARNING', 'message': 'Carga alta no processador'},
    {'timestamp': '2024-03-04 08:33:00', 'level': 'ERROR', 'message': 'Desconexão inesperada do cliente'},
    {'timestamp': '2024-03-04 08:34:00', 'level': 'INFO', 'message': 'Tarefa programada executada'},
    {'timestamp': '2024-03-04 08:35:00', 'level': 'ERROR', 'message': 'Falha na comunicação com API externa'},
    {'timestamp': '2024-03-04 08:36:00', 'level': 'DEBUG', 'message': 'Executando validação de dados'},
    {'timestamp': '2024-03-04 08:37:00', 'level': 'ERROR', 'message': 'Exceção não tratada no módulo de login'},
    {'timestamp': '2024-03-04 08:38:00', 'level': 'WARNING', 'message': 'Pico de acessos detectado'},
    {'timestamp': '2024-03-04 08:39:00', 'level': 'INFO', 'message': 'Servidor reiniciado corretamente'},
    {'timestamp': '2024-03-04 08:40:00', 'level': 'ERROR', 'message': 'Banco de dados corrompido'},
    {'timestamp': '2024-03-04 08:41:00', 'level': 'DEBUG', 'message': 'Monitorando consumo de recursos'},
    {'timestamp': '2024-03-04 08:42:00', 'level': 'ERROR', 'message': 'Falha no envio de dados para o servidor'},
    {'timestamp': '2024-03-04 08:43:00', 'level': 'INFO', 'message': 'Processo de sincronização finalizado'}
]

contagem_logs = []

for log in logs:
    if log['level'] == 'ERROR':
        contagem_logs.append(log)
        print(log['message'])

print(f"A quantidade de logs com severidade 'ERROR' é: {len(contagem_logs)}")


