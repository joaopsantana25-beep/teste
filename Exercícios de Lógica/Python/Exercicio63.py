'''
Exercicio 063
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''

lista=[]

while True:
    entrada=(input("Digite os números, para sair aperte enter: "))
    
    if entrada == '':
        break
    
    numero = float(entrada)

    if numero<0 or numero>1000:
        print('Número inválido, por favor digite valores de 0 a 1000')
        continue
    
    lista.append(numero)



if lista:
    print(f'O menor número digitado é {min(lista)}')

    print(f'O maior número digitado é {max(lista)}')

    print(f"A soma dos números digitados é {sum(lista)}")

else:
    print("Nenhum valor foi digitado")