'''
Exercicio 091
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
'''

n=int(input("Digite o termo n da série: "))


if n<=0:
    print("Digite um valor maior que 0")

else:
    soma =0
    for i in range(1,n+1):
        termo =  1/i
        soma+=termo
        print(f'{1}/{i}')

    print(f"\nSoma da série = {soma:.2f}")
