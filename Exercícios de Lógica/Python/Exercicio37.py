'''
Exercicio 037
Faça um Programa que leia um número inteiro maior que 0 e menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros.

Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades 12 = 1 dezena e 2 unidades

Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

numero = int(input("Digite um número entre 0 e 1000: "))

centenas = numero // 100
dezenas = (numero%100)//10
unidades = (numero%10)

if centenas<2:
    texto_centenas = "centena"

else:
    texto_centenas="centenas"

if dezenas<2:
    texto_dezenas = "dezena"

else:
    texto_dezenas="dezenas"


if unidades<2:
    texto_unidades = "unidade"

else:
    texto_unidades="unidades"




if centenas>=1 and dezenas>=1 and unidades>=1:
    print(f"{numero} = {centenas} {texto_centenas}, {dezenas} {texto_dezenas} e {unidades} {texto_unidades} ")

elif centenas>=1 and dezenas>=1 and unidades==0:
    print(f"{numero} = {centenas} {texto_centenas} e {dezenas} {texto_dezenas}"),

elif centenas>=1 and dezenas==0 and unidades>=1:
    print(f"{numero} = {centenas} {texto_centenas} e {unidades} {texto_unidades} ")

elif centenas>=1 and dezenas==0 and unidades==0:
    print(f"{numero} = {centenas} {texto_centenas} ")


elif centenas==0 and dezenas>=1 and unidades>=1:
    print(f"{numero} = {dezenas} {texto_dezenas} e {unidades} {texto_unidades}"),

elif centenas==0 and dezenas==0 and unidades>=1:
    print(f"{numero} = {unidades} {texto_unidades} ")

elif centenas==0 and dezenas>=1 and unidades==0:
    print(f"{numero} = {dezenas} {texto_dezenas} ")


