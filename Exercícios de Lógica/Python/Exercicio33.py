'''
Exercicio 033
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas: Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro; Triângulo Equilátero: três lados iguais; Triângulo Isósceles: quaisquer dois lados iguais; Triângulo Escaleno: três lados diferentes;
'''

lado1= float(input("Digite um lado do triângulo: "))

lado2= float(input("Digite um lado do triângulo: "))

lado3= float(input("Digite um lado do triângulo: "))

#Conferir se o triângulo é possível

if lado1+lado2>lado3 and lado1+lado3>lado2 and lado3+lado2>lado1:
    valido = True 

else:
    valido=False


if valido == True:
    if lado1==lado2 and lado1==lado3:
        print("Os valores podem formar um triângulo e ele será equilátero.")

    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print("Os valores podem formar um triângulo e ele será isósceles.")
    
    else:
        print("Os valores podem formar um triângulo e ele será escaleno. ")

else:
    print("Os valores não podem formar um triângulo.")