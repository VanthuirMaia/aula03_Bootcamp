# Integre na solução anterior um fluxo de While 
# que repita o fluxo até que o usuário insira as 
# informações corretas

# Solicita ao usuário que digite seu nome
# Validação do nome
nome_valido = False
while not nome_valido:
    try:
        nome = input("Digite seu nome: ").strip()

        if not nome:
            raise ValueError("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            nome_valido = True
    except ValueError as e:
        print(e)

# Validação do salário
salario_valido = False
while not salario_valido:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("O salário deve ser um valor positivo.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário. Digite um número válido.")

# Validação do bônus
bonus_valido = False
while not bonus_valido:
    try:
        bonus = float(input("Digite o valor do bônus recebido (exemplo: 0.10 para 10%): "))
        if bonus < 0:
            print("O bônus deve ser um valor positivo.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Digite um número válido.")

# Cálculo correto do bônus
bonus_recebido = salario * (1 + bonus)  # Considerando bônus percentual

# Exibição do resultado formatado
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")
