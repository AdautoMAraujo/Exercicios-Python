"""
co = float(input('Digite o comprimento do cateto oposto:\n'))
ca = float(input('digite o comprimento do cateto adjacente:\n'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa e igual a {hi:.2f}')
"""

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: \n'))
ca = float(input('Digite o comprimento do cateto adjacente: \n'))
print(f'A hipotenusa é igual a {hypot(co,ca):.2f}.')
