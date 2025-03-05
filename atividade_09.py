### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = [1, 2, 5, 8, 10, 11, 15, 19, 25, 33, 40]

num_pares = []
for numero in numeros:
    if numero % 2 == 0:
        num_pares.append(numero)

print(f"Total de numeros pares é: {len(num_pares)}")