count = 1
resultado = 1
num = int(input('Fatorial de: '))
while count <= num:
    resultado *= count
    count += 1
print(f'O fatorial de {num} é {resultado}.')

"""Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120"""