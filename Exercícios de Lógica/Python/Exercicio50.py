'''
Exercicio 050
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
'''


while True:

    pop_a = int(input("Digite o valor inicial da população da cidade A: "))
    pop_b = int(input("Digite o valor inicial da população da cidade B: "))


    taxa_a= float(input("Digite o valor da taxa de crescimento da população da cidade A: "))
    taxa_b= float(input("Digite o valor da taxa de crescimento da população da cidade B: "))

    if pop_a <= 0 or pop_b <= 0 or taxa_a <= 0 or taxa_b <= 0:
        print("Populações e taxas devem ser maiores que zero.")
        continue

    if taxa_a <= taxa_b and pop_a < pop_b:
        print("A população da cidade A nunca ultrapassará a da cidade B.")
    else:
        anos = 0

        while pop_a < pop_b:
                pop_a += pop_a * taxa_a
                pop_b += pop_b * taxa_b
                anos += 1
        
    
        print(f"Vai demorar {anos} anos para a população da cidade A ultrapassar ou igualar a da cidade B.")

    repetir = input("Deseja repetir a operação? (s/n): ").lower()
    if repetir != 's':
        break
   

#Versão ia

while True:
    pop_a = int(input("Digite a população inicial da cidade A: "))
    pop_b = int(input("Digite a população inicial da cidade B: "))

    taxa_a = float(input("Digite a taxa de crescimento da cidade A (ex: 0.03): "))
    taxa_b = float(input("Digite a taxa de crescimento da cidade B (ex: 0.015): "))

   

    
    


   