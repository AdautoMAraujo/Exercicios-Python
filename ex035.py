print('\033[33m-=\033[m' * 20)
print('\033[36;40m Analisando triangulos!!.\033[m')
print('\033[33m=_\033[m' * 20)
se1 = float(input('\033[33m Digíte o primeiro segmento:\033[m '))
se2 = float(input('\033[33m Digíte o segundo segmento:\033[m '))
se3 = float(input('\033[33m Digíte o terceiro segmento:\033[m '))
if se1 < se2 + se3 and se2 < se1 + se3 and se3 < se2 + se1:
    print(' \033[31m Os segmentos acima \033[7mPODEM\033[m \033[31mformar um \033[7mTRIANGULO!\033[m ')
else:
    print(' \033[31m Os segmentos acima \033[7mNÃO PODEM\033[m \033[31mformar um \033[7mTRIANGULO!!.\033[m ')
