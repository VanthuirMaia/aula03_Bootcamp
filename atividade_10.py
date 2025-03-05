### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# Lista de registros de vendas
vendas = [
    {"categoria": "Eletrônicos", "valor": 1500},
    {"categoria": "Roupas", "valor": 200},
    {"categoria": "Eletrônicos", "valor": 2300},
    {"categoria": "Alimentos", "valor": 100},
    {"categoria": "Roupas", "valor": 300},
    {"categoria": "Alimentos", "valor": 50},
]

# Dicionário para armazenar o total por categoria
total_por_categoria = {}

# Percorre a lista de vendas e soma os valores por categoria
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

# Exibir o total de vendas por categoria
print("Total de vendas por categoria:")
for categoria, total in total_por_categoria.items():
    print(f"{categoria}: R$ {total:.2f}")
