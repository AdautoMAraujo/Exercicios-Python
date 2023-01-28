km = float(input('Qual é a distancia da sua viagem?\n '))
print(f'Voçe está prestes a iniciar um viagem de {km}KM.')
if km >= 200:
    print(f'O preço da sua passagem será de R${km * 0.45 :.2f}.')
else:
    print(f'O preço da sua passagem será de R${km * 0.50 :.2f}.')
