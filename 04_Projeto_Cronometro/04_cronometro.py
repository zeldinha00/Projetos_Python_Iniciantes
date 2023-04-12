import time

t = input("Digite o tempo em (segundos): ")
    #tratando o digito com um numero inteiro
if t.isdigit():
    t = int(t)
else:
    print("Entrada Invalida")
    quit()
    #tratamento do cronometro usando divmod e time.sleep
while t:
    minutes, seconds = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1
print("Tempo Acabou!!!")