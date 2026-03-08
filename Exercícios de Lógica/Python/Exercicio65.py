'''
Exercicio 065
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

numero = int(input("Digite um número para descobrir se ele é primo ou não: "))
impar ='é primo'


if numero==1:
    print("O número 1 não é primo")

elif numero == 0:
    print("O número 0 não é primo")

else:
    for i in range (2,(numero)):
        if numero%i==0:
            impar="não é primo"
            break

    print(f"O número {numero} {impar}")


        