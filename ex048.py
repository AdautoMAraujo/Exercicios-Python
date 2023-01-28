soma = 0
calc = 0
for c in range(0, 501, 2):
    if c % 3 == 0:
        calc = calc + 1
        soma = soma + c
print(f'A soma de todos os {calc} valores equivale a {soma}.')
