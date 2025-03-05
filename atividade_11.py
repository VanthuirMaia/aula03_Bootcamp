### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

dados = []

while True:
    entrada = input("Digite um valor (ou 'sair' para encerrar): ").strip().lower()
    
    if entrada == "sair":
        break 
    dados.append(entrada)

print("\nDados inseridos:", dados)
