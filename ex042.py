se1 = float(input('Digite o primeiro segmento: '))
se2 = float(input('Digite o segundo seguimento: '))
se3 = float(input('digite o terceiro segmento: '))
if se1 < se2 + se3 and se2 < se1 + se3 and se3 < se2 + se1:
    print('Os segmentos acima PODEM formar um TRIANGULO ', end='')
    if se1 == se2 == se3:
        print('EQUILATERO.')
    elif se1 != se2 != se3 != se1:
        print('ESCALENO.')
    else:
        print('ISÓCELES.')
else:
    print('Os segmentos indicados NÃO PODEM formar um triangulo!.')
