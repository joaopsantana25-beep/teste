'''
Exercicio 077
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser 
informados também pelo usuário, conforme exemplo abaixo:

Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.'''


while True:
    numero = int(input("Digite o número que você deseja a tabuada: "))
    inicio = int(input("Qual o início da tabuada: "))
    fim = int(input("Qual o fim da tabuada: "))

    if fim<inicio:
        print("O final digitado é menor do que o início. Por favor digite um valor válido")
        continue

    print(f'\nVou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:')
    print("_ "*30)

    for i in range(inicio, fim+1):
        print(f'{numero} x {i} = {numero*i}')

    opcao = input("Você deseja fazer outra tabuada (s/n): ").lower()

    if opcao!='s':
        print("Terminando o programa")
        break

    