nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota:'))
media = (nota1 + nota2) / 2
print(f'Quem tirou {nota1:.1f} e {nota2:.1f} tem a média de {media:.1f}.')
if media < 5.0:
    print('E está REPROVADO!')
elif media < 6.9:
    print('E esta de RECUPERAÇÃO!')
elif media > 7.0:
    print('Voçe esta APROVADO!')
    print('Boas Férias!!')

"""– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO"""