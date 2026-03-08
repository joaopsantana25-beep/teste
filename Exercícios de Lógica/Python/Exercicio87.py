'''Exercicio 087
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.

O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média).


Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo: 
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
'''

while True:
    lista_de_saltos=[]
    
    nome_do_atleta=input("Digite o nome do atleta: ")

    if nome_do_atleta=='':
        print('Fim do Programa!')
        break

    for i in range(5):
        valor_salto=float(input(f"Digite o valor do {i+1}º salto : "))
        lista_de_saltos.append(valor_salto)

    print(f'Atleta: {nome_do_atleta}')
    print(f'\nPrimeiro Salto: {lista_de_saltos[0]:.1f} m')
    print(f'Segundo Salto: {lista_de_saltos[1]:.1f} m')
    print(f'Terceiro Salto: {lista_de_saltos[2]:.1f} m')
    print(f'Quarto Salto: {lista_de_saltos[3]:.1f} m')
    print(f'Quinto Salto: {lista_de_saltos[4]:.1f} m')

    print(f'\nMelhor salto: {max(lista_de_saltos)} m')
    print(f'Pior salto: {min(lista_de_saltos)} m')
    print(f'Media dos demais saltos = {(sum(lista_de_saltos)-max(lista_de_saltos)-min(lista_de_saltos))/3:.1f} m')

    print(f'\nResultado final: \n{nome_do_atleta}: {(sum(lista_de_saltos)-max(lista_de_saltos)-min(lista_de_saltos))/3:.2f} m')
    