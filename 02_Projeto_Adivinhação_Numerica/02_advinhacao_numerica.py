import random

# Jogo de advinhação numerica

print("Seja bem-vindo ao jogo de advinhação numerica!!!")

num_escolhido = input("Digite um número teto do desafio: ")

if num_escolhido.isdigit():
    num_escolhido = int(num_escolhido)
else:
    print("Erro: valor informado não é um numérico. Favor execute novamente e informe um número!")
    quit()

numero_randomico = random.randint(0 , num_escolhido)
tentativas = 0

while True:
    num_input = input("Adivinhe o número: ")
    if num_input.isdigit():
        num_input = int(num_input)
        tentativas += 1
    else:
        print("Erro: valor informado não é um numérico. Favor digite um número!")
        continue

    if num_input == numero_randomico:
        print("Acertou!")
        break
    elif num_input > numero_randomico:
        print("Valor muito alto, tente um mais baixo.")
    else:
        print("Valor muito baixo, tente um mais alto.")

print("Numero de tentativas: " + str(tentativas))