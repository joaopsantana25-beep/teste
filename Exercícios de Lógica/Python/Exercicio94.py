'''
Exercicio 094
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

notas=[]

for i in range(4):
    nota=float(input("Digite a sua nota: "))
    print("Nota computada")
    notas.append(nota)

for nota in notas:
    print(nota)

print(f"A media das notas é: {sum(notas)/len(notas):.2f}")