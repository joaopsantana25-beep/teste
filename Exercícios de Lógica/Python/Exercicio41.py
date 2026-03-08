'''
Exercicio 041
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.

O resultado da operação deve ser acompanhado de uma frase que diga se o número é: par ou ímpar; positivo ou negativo; inteiro ou decimal.
'''

num1 = float(input("Digite um número: "))

num2 = float(input("Digite um número: "))

operaçao=input("Digite a operação que você deseja fazer com esses números (som,sub,mul,div): ").lower()

if operaçao == "som":
    resultado = num1+num2

elif operaçao == "sub":
    resultado=num1-num2

elif operaçao == "mul":
    resultado=num1*num2

elif operaçao == "div":
    if num2==0:
        print("Operação inválida, segundo número é zero.")

    else:
        resultado = num1/num2

else:
    print("Digite um valor válido")


#Paridade, negatividade, inteiro

if resultado%2==0:
    paridade = "par"

else:
    paridade = "impar"

if resultado >0:
    sinal = "positivo"
    
elif resultado<0:
    sinal = "negativo"

else:
    sinal = "nulo"


if resultado == round(resultado):
    inteiro = "inteiro"

else:
    inteiro= "decimal"


print(f"O resultado da operação de {num1} com o {num2} é: {resultado}")
print(f"O número é {paridade}, {sinal} e {inteiro}.")
