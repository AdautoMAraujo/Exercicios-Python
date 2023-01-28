print('{:=^40}'.format(' LOJAS ARAUJO '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO 
[ 1 ] Á vista, Dinheiro/Cheque.
[ 2 ] Á vista no cartão.
[ 3 ] Em até 2X no cartão.
[ 4 ] 3X ou mais no cartão.   ''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2X de R${parcela:.2f} SEM JUROS.')
elif opção == 4:
    total = preço + (preço * 20/100)
    totpar = int(input('Quantas parcelas?' ))
    parcela = total / totpar
    print(f'Sua compra será parcelada em {totpar}X de R${parcela:.2f} COM JUROS.')
else:
    total = preço
    print('OPÇÃO INVALIDA tente novamente!')

print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')

