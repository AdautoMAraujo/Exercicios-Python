frase = str(input('Digíte uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso= ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('Não é um PALÍNDROMO!')
