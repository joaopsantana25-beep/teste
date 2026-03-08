'''
Exercicio 081
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.

Foram obtidos os seguintes dados: Código da cidade; Número de veículos de passeio (em 1999); Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber: Qual o maior e menor índice de acidentes de transito e a que cidade pertence; Qual a média de veículos nas cinco cidades juntas; Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''

maior_acidentes = -1
menor_acidentes = float('inf')
cidade_maior = cidade_menor = 0

total_veiculos = 0

total_acidentes_menos_2000=0
cont_menos_2000=0

for i in range(5):
    print(f"\nCidade {i+1}")
    codigo = int(input("Código da cidade: "))
    veiculos = int(input("Número de veículos de passeio: "))
    acidentes = int(input("Número de acidentes com vítimas: "))

    total_veiculos+=veiculos

    if acidentes>maior_acidentes:
        maior_acidentes=acidentes
        cidade_maior=codigo

    if acidentes<menor_acidentes:
        menor_acidentes=acidentes
        cidade_menor=codigo

    if veiculos <2000:
        total_acidentes_menos_2000+=acidentes
        cont_menos_2000+=1


media_veiculos = total_veiculos / 5

if cont_menos_2000 > 0:
    media_acidentes_menos_2000 = total_acidentes_menos_2000 / cont_menos_2000
else:
    media_acidentes_menos_2000 = 0

print("\nRESULTADOS")
print(f"Maior índice de acidentes: {maior_acidentes} - Cidade {cidade_maior}")
print(f"Menor índice de acidentes: {menor_acidentes} - Cidade {cidade_menor}")
print(f"Média de veículos nas cinco cidades: {media_veiculos:.2f}")
print(f"Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes_menos_2000:.2f}")