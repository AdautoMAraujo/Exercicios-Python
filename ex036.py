print('\033[34m==' * 15)
print('\033[31;107mSimulação de crédito imóvel!\033[m')
print('\033[34m==\033[m' * 15)
# Imputação de valores.
valor_casa = float(input('Qual o valor da casa, R$? '))
salario = float(input('Qual é o salário do comprador R$?'))
tempo = int(input('Em quanto tempo irá pagar? '))
# Depois faz as somas.
prestacao = valor_casa / (tempo * 12)
minimo = salario * 30/100
# Organização dos parametros.
print(f'Para pagar uma casa de R${valor_casa:.2f} em {tempo} anos,', end='')
print(f'a prestação sera de R${prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
