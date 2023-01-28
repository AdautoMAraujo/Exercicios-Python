from time import sleep
from random import randint
pc = randint(0, 5) #Faz o computador "escolher" um numero.
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5, tente advinhar!..')
print('-=-' * 20)
chute = int(input('Chute um numero:\n'))
print('PROCESSANDO....')
sleep(3)
if chute == pc:
    print('Meus parabens, voçe acertou!')
else:
    print('Voçe errou, mais sorte na proxima!.')
