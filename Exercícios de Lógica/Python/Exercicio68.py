'''Exercicio 068
Faça um programa que calcule o mostre a média aritmética de N notas.
'''
lista_de_notas=[]

while True:
    entrada = input("Digite as notas, para sair aperte enter: ")

    if entrada == '':
        break
    
    if not entrada.replace('.', '', 1).isdigit():
        print("Por favor digite um número")
        continue
    

    nota = float(entrada)

    lista_de_notas.append(nota)
    print("Nota contabilizada!")

if lista_de_notas:
    print(f'A média aritmética das notas é {sum(lista_de_notas)/len(lista_de_notas)}')

else:
    print("Nenhuma nota foi digitada")