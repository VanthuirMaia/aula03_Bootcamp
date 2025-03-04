### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

import random

# Gerar 300 registros de transações aleatórias
transacoes = [
    {"valor": random.randint(1, 20000), "hora": random.randint(0, 23)}
    for _ in range(301)
]

transacao_suspeita_valor = []  # Lista para transações suspeitas por valor
transacao_suspeita_hora = []   # Lista para transações suspeitas por horário

# Iterando sobre a lista de transações
for transacao in transacoes:
    # Verificando se o valor da transação é suspeito
    if transacao['valor'] > 10000:
        transacao_suspeita_valor.append(transacao)  # Adiciona à lista de valor
    
    # Verificando se a transação não foi marcada como suspeita pelo valor e se a hora é fora do horário comercial
    elif transacao['hora'] < 9 or transacao['hora'] > 18:
        if transacao not in transacao_suspeita_valor:  # Evita duplicidade
            transacao_suspeita_hora.append(transacao)  # Adiciona à lista de horário

# Exibindo as quantidades
print(f"Quantidade de transações suspeitas por valor: {len(transacao_suspeita_valor)}") # Total de transações suspeitas pelo valor
print(f"Quantidade de transações suspeitas por horário: {len(transacao_suspeita_hora)}") # Total de transações suspeitas pelo horário
print(f"Quantidade total de transações suspeitas: {len(transacao_suspeita_hora) + len(transacao_suspeita_valor)}") # Total de transações suspeitas