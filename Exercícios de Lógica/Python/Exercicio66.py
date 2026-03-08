'''
Exercicio 066
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
'''

numero = int(input("Digite um número para descobrir se ele é primo ou não: "))
impar ='é primo'
lista_de_divisores =[1,]
teste = True


if numero==1:
    print("O número 1 não é primo devido à definição de números primos")

elif numero == 0:
    print("O número 0 não é primo e ele é divisível por qualquer número diferente de 0")

else:
    for i in range (2,(numero)):
        if numero%i==0:
            impar="não é primo"
            teste=False
            lista_de_divisores.append(i)



if teste:
    print(f"O número {numero} {impar}")

else:
    lista_de_divisores.append(numero)
    print(f"O número {numero} {impar} e seus divisores são {lista_de_divisores}")


        