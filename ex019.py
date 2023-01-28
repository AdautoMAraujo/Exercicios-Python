import random
lista = input('Primeiro aluno:\n'), \
        input('Segundo aluno:\n'), \
        input('Terceiro aluno:\n'), \
        input('Quarto aluno:\n')
print(f'\nOs alunos participando são {lista}')
print(f'\nE o escolhido é {random.choices(lista)}')
