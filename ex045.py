from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'tesoura')
computador = randint(0, 2)
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA """)
player = int(input('Qual e a sua jogada? '))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('POO!!!')
print('-*-' * 10)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[player]}')
print('-*-' * 10)
if computador == 0:  # Computador jogou PEDRA.
    if player == 0:
        print('EMPATE!')
    elif player == 1:
        print('JOGADOR VENCE!')
    elif player == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVALIDA! Tente novamente.')
elif computador == 1:  # Computador jogou PAPEL.
    if player == 0:
        print('COMPUTADOR VENCE!')
    elif player == 1:
        print('EMPATE!')
    elif player == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVALIDA! Tente novamente.')
elif computador == 2:  # Computador jogou TESOURA.
    if player == 0:
        print('JOGADOR VENCE!')
    elif player == 1:
        print('COMPUTADOR VENCE!')
    elif player == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA! Tente novamente.')
else:
    print('Jogada invalida! Tente novamente.')