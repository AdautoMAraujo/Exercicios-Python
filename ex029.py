
km = float(input('Qual a velocidade do carro:\n'))
if km > 80:
    print('MULTADO, Voçe excedeu os limites de velocidade!')
    multa = (km - 80) * 7
    print(f'Voçe foi multado em R${multa}!!')
print('Tenha um bom dia, dirija com segurança!.')

