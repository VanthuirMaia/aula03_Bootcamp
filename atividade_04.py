### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

usuarios = [
    {'nome': 'Alice Silva', 'idade': 25, 'email': 'alice.silva@email.com'},  # Válido
    {'nome': 'Bruno Costa', 'idade': 17, 'email': 'bruno.costa@email.com'},  # Idade inválida (< 18)
    {'nome': 'Carlos Mendes', 'idade': 45, 'email': 'carlos.mendes@email.com'},  # Válido
    {'nome': 'Diana Souza', 'idade': 30, 'email': 'diana.souza.email.com'},  # E-mail inválido (falta @)
    {'nome': 'Eduardo Lima', 'idade': 66, 'email': 'eduardo.lima@email.com'},  # Idade inválida (> 65)
    {'nome': 'Fernanda Rocha', 'idade': 20, 'email': 'fernanda.rocha@email'},  # E-mail inválido (falta domínio)
    {'nome': 'Gabriel Santos', 'idade': 40, 'email': 'gabriel.santos@email.com'},  # Válido
    {'nome': 'Helena Martins', 'idade': 19, 'email': 'helena.martins@email.com'},  # Válido
    {'nome': 'Igor Ferreira', 'idade': 70, 'email': 'igor.ferreira@email.com'},  # Idade inválida (> 65)
    {'nome': 'Jéssica Almeida', 'idade': 50, 'email': 'jessica.almeidaemail.com'},  # E-mail inválido (falta @)
    {'nome': 'Kaio Oliveira', 'idade': 60, 'email': 'kaio.oliveira@email.com'},  # Válido
    {'nome': 'Larissa Nunes', 'idade': 22, 'email': 'larissa.nunes@email'},  # E-mail inválido (falta domínio)
    {'nome': 'Marcos Vieira', 'idade': 33, 'email': 'marcos.vieira@email.com'},  # Válido
    {'nome': 'Natália Castro', 'idade': 28, 'email': 'natalia.castro@email.com'},  # Válido
    {'nome': 'Otávio Lopes', 'idade': 67, 'email': 'otavio.lopes@email.com'},  # Idade inválida (> 65)
    {'nome': 'Paula Rodrigues', 'idade': 42, 'email': 'paula.rodrigues@email.com'},  # Válido
    {'nome': 'Ricardo Barros', 'idade': 15, 'email': 'ricardo.barros@email.com'},  # Idade inválida (< 18)
    {'nome': 'Sofia Pereira', 'idade': 26, 'email': 'sofia.pereira.email.com'},  # E-mail inválido (falta @)
    {'nome': 'Thiago Mendes', 'idade': 35, 'email': 'thiago.mendes@email.com'},  # Válido
    {'nome': 'Vanessa Cardoso', 'idade': 29, 'email': 'vanessa.cardoso@email.com'}  # Válido
]

usuarios_validos = []
usu_menor_18 = []
usu_maior_65 = []
usu_email_invalido = []

for usuario in usuarios:
    erros = []
    
    if usuario['idade'] < 18:
        usu_menor_18.append(usuario)
        erros.append("Idade menor que 18 anos")
    
    if usuario['idade'] > 65:
        usu_maior_65.append(usuario)
        erros.append("Idade maior que 65 anos")
    
    if '@' not in usuario['email'] or '.' not in usuario['email'].split('@')[-1]:
        usu_email_invalido.append(usuario)
        erros.append("E-mail inválido")
    
    if erros:
        print(f"Erro(s) encontrado(s) para {usuario['nome']}: {', '.join(erros)}")
    else:
        usuarios_validos.append(usuario)

# Exibição dos resultados organizados
print("\n--- Resumo da Validação ---")
print(f"✅ {len(usuarios_validos)} usuários válidos.")
print(f"❌ {len(usu_menor_18)} usuários com idade menor que 18 anos.")
print(f"❌ {len(usu_maior_65)} usuários com idade maior que 65 anos.")
print(f"❌ {len(usu_email_invalido)} usuários com e-mail inválido.")

# Exibição dos usuários inválidos por categoria
if usu_menor_18:
    print("\n🔴 Usuários com idade menor que 18 anos:")
    for u in usu_menor_18:
        print(f"- {u['nome']} ({u['idade']} anos)")

if usu_maior_65:
    print("\n🔴 Usuários com idade maior que 65 anos:")
    for u in usu_maior_65:
        print(f"- {u['nome']} ({u['idade']} anos)")

if usu_email_invalido:
    print("\n🔴 Usuários com e-mail inválido:")
    for u in usu_email_invalido:
        print(f"- {u['nome']} ({u['email']})")

print("\n✅ Dados verificados com sucesso!")
