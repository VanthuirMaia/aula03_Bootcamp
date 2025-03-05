### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

def normalizar(lista):
    X_min = min(lista)
    X_max = max(lista)
    return [(x - X_min) / (X_max - X_min) for x in lista]

# Exemplo de uso
numeros = [10, 20, 30, 40, 50]
numeros_normalizados = normalizar(numeros)

print(numeros_normalizados)
