import random
import string

def password_generator(len_pass = 8):
    ascii_options = string.ascii_letters #variavel que busca todas letras do alfabeto ascii
    number_options = string.digits  #varivel que pega todos digitos
    punt_options = string.punctuation #variavel que pega todas pontuação
    options = ascii_options + number_options + punt_options #Colocar todas variaveis em uma variavel

    password_user = ""

    for i in range(0, len_pass):
        digit = random.choice(options)
        password_user += digit

    return password_user #retorna a função com os digitos

choice_user = input("Quantos digitos na senha?")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada invalida")
    quit()

response = password_generator(len_pass=choice_user)
print(f"Senha gerada:\n{response}")
