# ### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

vendas = {
    "Produto_1": {"quantidade": 10, "preço": 15.50},
    "Produto_2": {"quantidade": 5, "preço": 20.00},
    "Produto_3": {"quantidade": 3, "preço": 25.30},
    "Produto_4": {"quantidade": 8, "preço": 12.75},
    "Produto_5": {"quantidade": 15, "preço": 30.40},
    "Produto_6": {"quantidade": 7, "preço": 18.60},
    "Produto_7": {"quantidade": -12, "preço": 22.80},
    "Produto_8": {"quantidade": 6, "preço": 28.90},
    "Produto_9": {"quantidade": 10, "preço": 19.50},
    "Produto_10": {"quantidade": 4, "preço": 17.00},
    "Produto_11": {"quantidade": 20, "preço": 5.99},
    "Produto_12": {"quantidade": 11, "preço": 14.90},
    "Produto_13": {"quantidade": 9, "preço": 16.75},
    "Produto_14": {"quantidade": 13, "preço": 27.20},
    "Produto_15": {"quantidade": 16, "preço": 23.50},
    "Produto_16": {"quantidade": 14, "preço": 11.45},
    "Produto_17": {"quantidade": 5, "preço": -26.90},
    "Produto_18": {"quantidade": 8, "preço": 21.60},
    "Produto_19": {"quantidade": 2, "preço": 33.10},
    "Produto_20": {"quantidade": 3, "preço": 29.99},
    "Produto_21": {"quantidade": 10, "preço": 17.85},
    "Produto_22": {"quantidade": 6, "preço": 24.60},
    "Produto_23": {"quantidade": 7, "preço": 31.00},
    "Produto_24": {"quantidade": 9, "preço": 13.25},
    "Produto_25": {"quantidade": 12, "preço": 20.30},
    "Produto_26": {"quantidade": 15, "preço": 10.50},
    "Produto_27": {"quantidade": 4, "preço": 18.95},
    "Produto_28": {"quantidade": 11, "preço": 21.15},
    "Produto_29": {"quantidade": 2, "preço": 28.50},
    "Produto_30": {"quantidade": 8, "preço": 32.90},
    "Produto_31": {"quantidade": 10, "preço": 14.30},
    "Produto_32": {"quantidade": -6, "preço": 25.80},
    "Produto_33": {"quantidade": 13, "preço": 9.99},
    "Produto_34": {"quantidade": 7, "preço": 22.45},
    "Produto_35": {"quantidade": 5, "preço": 16.90},
    "Produto_36": {"quantidade": 4, "preço": 34.40},
    "Produto_37": {"quantidade": 3, "preço": 19.75},
    "Produto_38": {"quantidade": 9, "preço": 23.10},
    "Produto_39": {"quantidade": 14, "preço": 28.20},
    "Produto_40": {"quantidade": 12, "preço": 30.15},
    "Produto_41": {"quantidade": 11, "preço": -11.50},
    "Produto_42": {"quantidade": 15, "preço": 27.60},
    "Produto_43": {"quantidade": 10, "preço": 15.00},
    "Produto_44": {"quantidade": 8, "preço": 33.20},
    "Produto_45": {"quantidade": 7, "preço": 22.90},
    "Produto_46": {"quantidade": 12, "preço": 20.90},
    "Produto_47": {"quantidade": 9, "preço": 12.50},
    "Produto_48": {"quantidade": 10, "preço": 18.70},
    "Produto_49": {"quantidade": 3, "preço": 21.00},
    "Produto_50": {"quantidade": 14, "preço": 23.80}
}


def verificar_dados(vendas):
    for produto, dados in vendas.items():
        quantidade = dados["quantidade"]
        preco = dados["preço"]
        if quantidade > 0 and preco > 0:
            print(f"{produto}: Dados válidos")
        else:
            print(f"{produto}: Dados inválidos")

verificar_dados(vendas)



