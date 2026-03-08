'''
Exercicio 034
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c.

O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo
    grau e o programa não deve fazer pedir os demais valores,
    sendo encerrado;

Se o delta calculado for negativo, a equação não possui raízes reais.
    Informe ao usuário e encerre o programa;

Se o delta calculado for igual a zero a equação possui apenas uma raiz
    real; informe-a ao usuário;

Se o delta for positivo, a equação possui duas raiz reais;
    informe-as ao usuário;
    
'''

a = float(input("Digite o coeficiente de x²: "))
b = float(input("Digite o coeficiente que acompanha x: "))
c = float(input("Digite o coeficiente independente: "))

def delta():
    delta = b**2 - 4*a*c

    if a ==0:
        print("A equação não é do segundo grau.\nFinalizando o Programa")
    
    else:
        if delta<0:
            print("A equação não possui raízes reais\nFinalizando o programa")
    
        elif delta>0:
            x1=(-b+delta**0.5)/2*a
            x2=(-b-delta**0.5)/2*a 
            print(f"A equação possui duas raízes reais {x1} e {x2}\nFinalizando o programa")

        elif delta == 0:
            x1=(-b+delta**0.5)/2*a
            print(f"A equação possui apenas uma raíz real {x1}\nFinalizando o programa")

delta()