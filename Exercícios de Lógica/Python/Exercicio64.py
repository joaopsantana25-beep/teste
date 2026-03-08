'''
Exercicio 064
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''
while True:
    numero=int(input("Digite o número para encontrar seu fatorial: "))
    fatorial = 1

    if numero<0:
        print("Não existe fatorial de número negativo")
        continue

    elif numero ==0:
        print("0! = 1")
        continue

    elif numero>16:
        print("Por favor digite número menores que 16")
        continue
    
    for i in range (1,numero+1):
        fatorial=fatorial*i

    print(f'{numero}! = {fatorial}')