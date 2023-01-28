from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for nasc in range(1, 7+1):
    pess = int(input(f'Informe a data de nascimento da {nasc}º pessoa: '))
    idade = atual - pess
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print(f'Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'E tambem tivemos {menores} pessoas menores de idade')
