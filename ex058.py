from time import sleep
from random import randint
pc = randint(0, 10)
total = 0
print('-=' * 15)
print('Vou escolher um número de "0" a "10", tente advinhar!!')
print('-=' * 15)
c = int(input('Chute um número de "0" a "10": '))
total += 1
print('PROCESSANDO PALPITE!!!')
sleep(1)
while c != pc:
    c = int(input('Voçe errou!! Tente novamente: '))
    total += 1
    if c < pc:
        print('Chute mais alto!')
    if c > pc:
        print('Chute mais baixo!')
print('Voçe acertou!. Meus parabens!')
print(f' Voçe precisou de {total} chutes para acertar')
