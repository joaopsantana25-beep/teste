'''
Exercicio 048
Faça um programa que leia e valide as seguintes informações: 
Nome: maior que 3 caracteres; Idade: entre 0 e 150; 
Salário: maior que zero;
Sexo: 'f' ou 'm'; 
Estado Civil: 's', 'c', 'v', 'd';
'''

while True:
    contador = 0

    nome = input("Digite o seu nome: ")

    idade = int(input("Digite a sua idade: "))

    salario = float(input("Digite o seu salário: "))

    sexo = input("Digite o seu sexo (f/m): ").lower()

    estado_civil=input("Digite seu estado civil (s, c, v, d): ").lower()

    if len(nome)>3:
        print("Nome válido")
        contador+=1
    
    else:
        print("Nome inválido. Ele deve ser maior do que 3 caracteres")
    

    if idade>0 and idade<=150:
        print("Idade válida")
        contador+=1

    else:
        print("Idade inválida. Ela deve estar entre 0 e 150(incluindo)")

    if salario>0:
        print("Salário válido")
        contador+=1

    else:
        print("Salário inválido. Ele deve ser maior que 0")

    if sexo in "fm":
        print("Sexo válido")
        contador+=1
    
    else:
        print("Sexo inválido. Coloque 'f' para feminino e 'm' para masculino")

    if estado_civil in "scvd":
        print("Estado Civil válido")
        contador+=1
    
    else:
        print("Estado civil inválido. Coloque 's','c','v','d' " )

    if contador ==5:
        print("Todas as informações estão válidas")
        print("Fim do programa")
        break