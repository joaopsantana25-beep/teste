'''Exercicio 088
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. 
A sua nota fica sendo a média dos votos restantes.

Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação 
e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a 
média com as notas restantes).

As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo: 

Atleta: Aparecido Parente Nota: 9.9 Nota: 7.5 Nota: 9.5 Nota: 8.5 Nota: 9.0 Nota: 8.5 Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
'''

while True:
    lista_de_notas=[]
    
    nome_do_atleta=input("\nDigite o nome do atleta: ")

    if nome_do_atleta=='':
        print('Fim do Programa!')
        break

    for i in range(7):
        nota=float(input(f"Digite o valor da {i+1}ª nota : "))
        lista_de_notas.append(nota)

    print(f'\nAtleta: {nome_do_atleta}')
    for i in range(7):
        print(f'Nota: {lista_de_notas[i]}')

    print('\nResultado final:')
    print(f'Atleta: {nome_do_atleta}')
    print(f"Melhor nota: {max(lista_de_notas)}")
    print(f'Pior nota: {min(lista_de_notas)}')
    print(f'Media:{(sum(lista_de_notas)-max(lista_de_notas)-min(lista_de_notas))/5:.2f} ')