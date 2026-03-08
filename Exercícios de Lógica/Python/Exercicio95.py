'''
Exercicio 095
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

vogais = "aeiou"
numero_de_consoantes = 0

print("Digite 10 caracteres:")

for i in range(10):
    caracter = input(f"Caractere {i+1}: ").lower()

    # Verifica se é letra e se é consoante
    if caracter.isalpha() and caracter not in vogais:
        numero_de_consoantes += 1
        print(f"Consoante encontrada: {caracter}")

print(f"\nTotal de consoantes digitadas: {numero_de_consoantes}")