'''
Exercicio 104
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

temperaturas = [
    30.5,  # Janeiro
    30.1,  # Fevereiro
    29.0,  # Março
    27.5,  # Abril
    25.0,  # Maio
    23.5,  # Junho
    22.8,  # Julho
    24.0,  # Agosto
    25.5,  # Setembro
    27.0,  # Outubro
    28.5,  # Novembro
    29.8   # Dezembro
]

media = sum(temperaturas)/len(temperaturas)

print(f"{'Mês':<12} | {'Temperatura'}")
print("-" * 25)

for mes,temperatura in zip(meses,temperaturas):
    if temperatura>media:
        print(f"{mes:<12} - {temperatura:>6.1f}°C")