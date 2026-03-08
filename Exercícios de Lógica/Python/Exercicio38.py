'''
Exercicio 038
Faça um Programa para um caixa eletrônico.

O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.

As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.

O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

numero = int(input("Digite o valor para ser sacado: "))
partes=[]

notas_100 = numero//100

if notas_100==1:
    texto_100="nota"

else:
    texto_100="notas"


notas_50 = (numero%100)//50

if notas_50==1:
    texto_50="nota"

else:
    texto_50="notas"


notas_10 = ((numero%100)%50)//10

if notas_10==1:
    texto_10="nota"

else:
    texto_10="notas"


notas_5 = (((numero%100)%50)%10)//5

if notas_5==1:
    texto_5="nota"

else:
    texto_5="notas"


notas_1=(((numero%100)%50)%10)%5

if notas_1==1:
    texto_1="nota"

else:
    texto_1="notas"




if notas_100 > 0:
    partes.append((f"{notas_100} {texto_100} de 100"))
if notas_50 > 0:
    partes.append(f"{notas_50} {texto_50} de 50")
if notas_10 > 0:
    partes.append(f"{notas_10} {texto_10} de 10")
if notas_5 > 0:
    partes.append(f"{notas_5} {texto_5} de 5")
if notas_1 > 0:
    partes.append(f"{notas_1} {texto_1} de 1")


resultado = f"Para sacar a quantia de {numero} reais, o programa fornece "

resultado += ", ".join(partes)

print(resultado)