n1 = int(input('\033[31mPrimeiro numero: '))
n2 = int(input('\033[31mSegundo numero: '))
if n1 > n2:
    print(f'\033[34mO número {n1} é maior que {n2}.')
elif n2 > n1:
    print(f'\033[34mO numero {n2} é maior que {n1}.')
else:
    print(f'\033[35mOs dois números são iguais!')
