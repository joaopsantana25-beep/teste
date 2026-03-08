'''
Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9)

'''

def celsius(farenheit):
    C = (5*(farenheit-32)/9)
    return C 

f = float(input("Digite a temperatura em °F: "))


print(f"A temperatura em celsius é {celsius(f)}°C")
    