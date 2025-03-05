### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# Exemplo de uso
usuarios = [
    {"nome": "João", "idade": 25, "email": "joao@email.com"},
    {"nome": "Claudio", "idade": 30},  # Sem email
    {"nome": "Dulce", "idade": 22, "email": "dulce@email.com"},
    {"nome": "Vanessa", "email": "vanessa@email.com"}  # Sem idade
]

def filtrar_dados_faltantes(lista, campos):
    return [dado for dado in lista if all(campo in dado for campo in campos)]

usuarios_filtrados = filtrar_dados_faltantes(usuarios, ["email", "idade"])

print(usuarios_filtrados)
