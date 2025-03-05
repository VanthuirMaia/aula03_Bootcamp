### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# Simulação de uma API paginada
def api_simulada(pagina):
    """Simula uma API que retorna dados paginados."""
    dados = {
        1: ["item1", "item2", "item3"],
        2: ["item4", "item5", "item6"],
        3: ["item7", "item8", "item9"],
        4: ["item10"],
    }
    return {"dados": dados.get(pagina, []), "proxima_pagina": pagina + 1 if pagina in dados else None}

todos_os_dados = []
pagina_atual = 1

while pagina_atual is not None:
    resposta = api_simulada(pagina_atual)
    todos_os_dados.extend(resposta["dados"])
    pagina_atual = resposta["proxima_pagina"]

print("Todos os dados coletados da API:", todos_os_dados)
