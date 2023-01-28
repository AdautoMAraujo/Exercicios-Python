soma = 0
cont = 0
for c in range(1, 6+1):
    num = int(input(f'Digíte o {c}º numero: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Voçe informou {cont} números PARES e a soma entre eles é {soma}.')
