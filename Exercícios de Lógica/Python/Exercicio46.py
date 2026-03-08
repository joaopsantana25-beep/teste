'''Exercicio 046
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e 
continue pedindo até que o usuário informe um valor válido.
'''

while True:
    nota = float(input("\nDigite uma nota de 0 a 10: "))

    if nota>=0 and nota<=10:
        print(f"Você digitou {nota}")
        print("Finalizando o Programa")
        break

    else:
        print("\nPor favor digite uma nota válida")