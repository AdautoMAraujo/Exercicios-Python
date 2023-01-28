nr = int(input('Informe um nomero:\n'))
u = nr // 1 % 10
d = nr // 10 % 10
c = nr // 100 % 10
m = nr // 1000 % 10
print(f'Analisando o numero {nr}')
print(f'A Unidade é {u}')
print(f'A Dezena é {d}')
print(f'A Centena é {c}')
print(f'o Milhar é {m}')


