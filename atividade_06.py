### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# O texto pode vir de outras fontes, sendo importado de um arquivo pdf ou docx por exemplo, através da biblioteca: PyPDF2 ou pdfplumber e python-docx.

import string

# O texto pode ser digitado pelo usuário, ou ser fixo no código.
texto = input("Digite um texto: ")  # Recebe o texto

# Remove pontuação e converte o texto para minúsculas
texto = texto.translate(str.maketrans('', '', string.punctuation)).lower()

# Dividindo o texto em palavras
palavras = texto.split()

# Contando as ocorrências de cada palavra (usando um dicionário)
contagem_palavras = {}  # Agora é um dicionário, e não uma lista
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

# Classificando as palavras pela contagem, do maior para o menor
palavras_classificadas = sorted(contagem_palavras.items(), key=lambda x: x[1], reverse=True)

# Resultado
print("Contagem de palavras no texto (classificadas):")
for palavra, contagem in palavras_classificadas:
    print(f"A palavra '{palavra}' aparece {contagem} vezes.")
