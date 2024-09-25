import json

with open('faturamento.json','r') as file:
    dados = json.load(file)

faturamento_diario = dados['faturamento_diario']

faturamentos = [valor for valor in faturamento_diario if valor > 0]
menor = min(faturamentos)
maior = max(faturamentos)
media = sum(faturamentos) / len(faturamentos)
dias_acima_media = sum(1 for valor in faturamento_diario if valor > media)

print(f"Menor valor de faturamento:{menor}")
print(f"Maior valor de faturamento:{maior}")
print(f"Número de dias com faturamento acima da média:{dias_acima_media}")
