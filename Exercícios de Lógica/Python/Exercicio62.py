'''
Exercicio 062
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''
lista=[]

while True:
    entrada=(input("Digite os números, para sair aperte enter: "))
    
    if entrada == '':
        break

    numero = float(entrada)

    lista.append(numero)



if lista:
    print(f'O menor número digitado é {min(lista)}')

    print(f'O maior número digitado é {max(lista)}')

    print(f"A soma dos números digitados é {sum(lista)}")

else:
    print("Nenhum valor foi digitado")