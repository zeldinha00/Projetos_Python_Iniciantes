import random

#Jogo Pedra, Papel, Tesoura

user_points = 0
computer_points = 0

options = ["r", "p", "t"]

while True:
    user_choiser = input("""Escolha uma das seguites opções:
    (R) - PEDRA
    (P) - PAPEL
    (T) - TESOURA
    (Q) SAIR
    => """).lower()
    # tratamento para sair do jogo
    if user_choiser == "q":
        break
    # tratamento para opções
    if user_choiser not in options:
        continue
    # numero randomico para o computador
    computer_choiser =  random.randint(0,2)
    # ( 0 = R , 1 = P , 2 = T )
    # tratamento de inteiro para srt
    computer_option = options[computer_choiser]

    #tratamento das opções pedra papel tesoura

    if user_choiser ==  computer_option:
        print("Empatou!")
    elif user_choiser == "r" and computer_option == "t":
        print("Você venceu!!!")
        user_points += 1
    elif user_choiser == "p" and computer_option == "r":
        print("Você venceu!!!")
        user_points += 1
    elif user_choiser == "t" and computer_option == "p":
        print("Você venceu!!!")
        user_points += 1
    else:
        print("Voceê Perdeu!!!")
        computer_points += 1

print("Sua Pontuação: " + str(user_points))
print("Pontuação do computador: " + str(computer_points))

# tratamento para final

if user_points > computer_points:
    print("VITORIA")
elif user_points == computer_points:
    print("EMPATOU")
else:
    print("DERROTA")