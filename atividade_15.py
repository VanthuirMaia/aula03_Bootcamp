### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

# Lista de dados
dados = [10, 20, 30, 40, 50, 60, 70, 80, 90, 99, 100]

# Valor de parada
valor_de_parada = 99

# Processamento dos dados
for item in dados:
    if item == valor_de_parada:
        print("Processamento interrompido!")
        break  
    print(f"Processando item: {item}")
