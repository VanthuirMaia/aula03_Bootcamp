### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

temperaturas = {
    "Sensor_1": 16.5, "Sensor_2": 22.3, "Sensor_3": 30.1, "Sensor_4": 18.2, "Sensor_5": 25.5,
    "Sensor_6": 17.8, "Sensor_7": 19.1, "Sensor_8": 28.4, "Sensor_9": 15.0, "Sensor_10": 23.7,
    "Sensor_11": 29.9, "Sensor_12": 14.6, "Sensor_13": 21.5, "Sensor_14": 24.9, "Sensor_15": 27.8,
    "Sensor_16": 17.0, "Sensor_17": 26.0, "Sensor_18": 13.5, "Sensor_19": 20.7, "Sensor_20": 30.5,
    "Sensor_21": 16.9, "Sensor_22": 22.2, "Sensor_23": 25.1, "Sensor_24": 18.4, "Sensor_25": 20.0,
    "Sensor_26": 29.4, "Sensor_27": 17.3, "Sensor_28": 23.6, "Sensor_29": 12.8, "Sensor_30": 26.5,
    "Sensor_31": 15.2, "Sensor_32": 21.0, "Sensor_33": 30.0, "Sensor_34": 18.7, "Sensor_35": 19.5,
    "Sensor_36": 14.3, "Sensor_37": 27.1, "Sensor_38": 23.8, "Sensor_39": 28.2, "Sensor_40": 26.8,
    "Sensor_41": 20.3, "Sensor_42": 17.9, "Sensor_43": 18.9, "Sensor_44": 30.3, "Sensor_45": 16.0,
    "Sensor_46": 24.2, "Sensor_47": 20.9, "Sensor_48": 22.1, "Sensor_49": 26.2, "Sensor_50": 29.2,
    "Sensor_51": 16.1, "Sensor_52": 22.9, "Sensor_53": 18.3, "Sensor_54": 19.2, "Sensor_55": 27.5,
    "Sensor_56": 14.1, "Sensor_57": 21.8, "Sensor_58": 25.0, "Sensor_59": 28.9, "Sensor_60": 19.8,
    "Sensor_61": 30.7, "Sensor_62": 20.6, "Sensor_63": 16.4, "Sensor_64": 23.4, "Sensor_65": 17.2,
    "Sensor_66": 18.8, "Sensor_67": 28.7, "Sensor_68": 15.6, "Sensor_69": 21.3, "Sensor_70": 25.8,
    "Sensor_71": 30.6, "Sensor_72": 19.3, "Sensor_73": 17.7, "Sensor_74": 26.4, "Sensor_75": 22.6,
    "Sensor_76": 18.6, "Sensor_77": 24.5, "Sensor_78": 27.0, "Sensor_79": 29.1, "Sensor_80": 14.7,
    "Sensor_81": 21.7, "Sensor_82": 22.8, "Sensor_83": 27.6, "Sensor_84": 30.4, "Sensor_85": 25.7,
    "Sensor_86": 19.6, "Sensor_87": 16.8, "Sensor_88": 29.6, "Sensor_89": 12.9, "Sensor_90": 18.0,
    "Sensor_91": 24.3, "Sensor_92": 20.5, "Sensor_93": 26.3, "Sensor_94": 15.4, "Sensor_95": 23.1,
    "Sensor_96": 17.4, "Sensor_97": 21.9, "Sensor_98": 28.5, "Sensor_99": 20.8, "Sensor_100": 14.4
}

# Inicializando as listas
temp_baixa = []
temp_normal = []
temp_alta = []

# Iterando sobre os sensores e suas temperaturas
for sensor, temperatura in temperaturas.items():
    if temperatura < 18:
        temp_baixa.append(sensor)
        print(f"O {sensor} está com a temperatura de {temperatura}°C Considerada Baixa")
    elif temperatura >= 18 and temperatura <= 26:
        temp_normal.append(sensor)
        print(f"O {sensor} está com a temperatura de {temperatura}°C Considerada Normal")
    else:
        temp_alta.append(sensor)
        print(f"O {sensor} está com a temperatura de {temperatura}°C Considerada Alta")

# Contagem dos sensores em cada categoria
print(f"A quantidade de sensores com temperatura baixa é: {len(temp_baixa)}")
print(f"A quantidade de sensores com temperatura normal é: {len(temp_normal)}")
print(f"A quantidade de sensores com temperatura alta é: {len(temp_alta)}")


