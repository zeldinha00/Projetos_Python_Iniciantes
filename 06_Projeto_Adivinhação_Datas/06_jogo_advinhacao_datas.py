import json
import random

f = open("words.json", encoding="utf8")

words = json.load(f)
choice_c = random.choice(list(words.keys()))

print("Ola, seja bem vindo!")
print("#################################")

#variavel numero de tentativas
n_choices = 5
win = False

while n_choices > 0 and win is not True:
    print("Dica: " + words[choice_c])
    answer_user = input("Data: DDMMAAAA\n")
    print("################## \n")

    if len(answer_user) != 8:  #tratamento se não tiver 8 digitos
        print("Erro na entrada. A resposta deve conter 8 digitos.")
        continue

    if answer_user.isdigit():
        check = []
        pontuation = 0
        for i in range(8):  #tratamento se o digito é igual a resposta
            if answer_user[i] == choice_c[i]:
                check.append("✅")
                pontuation += 1
            else:
                check.append("💢")

        print("Resposta: \n")
        print("|".join(check))
        print(" |".join(answer_user))
        print("#######################\n")

        if pontuation == 8: # tratamento se ele acerta os 8 digitos
            win = True

    else:   # tratamento que deve ser uma data
        print("Erro na entrada. A resposta deve ser uma data.")
        continue
    n_choices -= 1  #tratamento que ele perde 1 chance

if win == True:    #tratamento fora do laço onde determina vitoria ou derrota e mostra a resposta.
    print("VITÓRIA!!!")
else:
    print("DERROTA!")
    print("A resposta era: " + choice_c)