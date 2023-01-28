from random import shuffle
n1 = input('Nome do Aluno:\n')
n2 = input('Nome do Aluno:\n')
n3 = input('Nome do aluno:\n')
n4 = input('Nome do aluno:\n')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação é: {lista}')


"""import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(f'A ordem da apresentação será: ')
print('=' * 50)
print(lista)"""


