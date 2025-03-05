### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

tentativas_maximas = 5 
tentativa = 1  

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}")
    
    if True:
        print("Conexão bem-sucedida!")
        break
    
    tentativa += 1
else:
    print("Falha ao conectar após várias tentativas.")
