"""list = []
for p in range(1, 6):
    peso = float(input(f'Peso da {p}º pessoa: '))
    list = [peso]
print(f'O maior peso foi {max(list)}')
print(f'O menor peso foi {min(list)}')"""

pesos = [float(input(f'Peso da {a}º pessoa: ')) for a in range(1, 6)]
print(f'O maior peso foi de {max(pesos)}Kg\n'
      f'O menor foi de {min(pesos)}Kg!')
