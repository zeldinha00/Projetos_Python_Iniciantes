# Projeto 01 - Quiz

print("Seja bem-vindo ao Quiz!!!")
start_quiz = input("Deseja iniciar o QUIZ? S/N \n").lower()

if start_quiz != "s":
    quit()
pontuacao = 0

print("Começando...")
pergunta1 = input("""1) Qual é a sintaxe correta para imprimir a frase "Olá, mundo!" em Python?
 a) print("Hello, world!")
 b) print("Olá, mundo!")
 c) echo("Olá, mundo!")
 d) write("Olá, mundo!")
""").lower()

if pergunta1 == "b":
    print(f"---Resposta: {pergunta1}, correta!---")
    pontuacao += 1
else:
    print(f"---Resposta: {pergunta1}, Incorreta---")

pergunta2 = input("""2) Qual é o operador lógico usado em Python para representar a negação?
 a) &&
 b) !
 c) ||
 d) ~
""").lower()

if pergunta2 == "b":
    print(f"---Resposta: {pergunta2}, correta!---")
    pontuacao += 1
else:
    print(f"---Resposta: {pergunta2}, Incorreta---")

pergunta3 = input("""3) Em Python, qual é a função usada para obter o comprimento de uma string?
 a) length()
 b) count()
 c) len()
 d) size()
""").lower()

if pergunta3 == "c":
    print(f"---Resposta: {pergunta3}, correta!---")
    pontuacao += 1
else:
    print(f"---Resposta: {pergunta3}, Incorreta---")

pergunta4 = input("""3) Qual é a palavra-chave usada em Python para definir uma função?
 a) def
 b) func
 c) define
 d) fun
""").lower()

if pergunta4 == "a":
    print(f"---Resposta: {pergunta4}, correta!---")
    pontuacao += 1
else:
    print(f"---Resposta: {pergunta4}, Incorreta---")

pergunta5 = input("""3) Qual é a função usada em Python para ler dados do teclado?
 a) read()
 b) input()
 c) get()
 d) type()
""").lower()

if pergunta5 == "b":
    print(f"---Resposta: {pergunta5}, correta!---")
    pontuacao += 1
else:
    print(f"---Resposta: {pergunta5}, Incorreta---")


if pontuacao > 3:
    print(f"Você foi muito bem, sua pontuação foi: {pontuacao}/5")
else:
    print(f"Você teve a nota fraca, sua pontuação foi: {pontuacao}/5")

print("####  Fim do QUIZ  ####")




