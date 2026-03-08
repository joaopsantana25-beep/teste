'''
Exercicio 047
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    nome_usuario = input("Digite o nome do seu usuário: ")

    senha_usuario = input("Digite a senha: ")

    if senha_usuario==nome_usuario:
        print("\nPor favor digite uma senha diferente do nome do usuário.")

    else:
        print("Nome e senha válidos!")
        print("Finalizando o programa!")
        break