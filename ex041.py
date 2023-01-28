from datetime import date
atual = date.today().year
nasc = int(input('Data de nascimento do atleta: '))
idade = atual - nasc
print(f'Uma pessoa que nasceu em {nasc}, tem agora {idade} anos.')
if idade <= 9:
    print(f'Se enquadra na categoria de atleta MIRIM.')
elif idade <= 14:
    print(f'Se enquadra na categoria de atleta INFANTIL.')
elif idade <= 19:
    print(f'Se enquadra na categoria de atleta JÚNIOR.')
elif idade <= 25:
    print(f'Se enquadra na categoria de atleta SÊNIOR.')
elif idade > 25:
    print(f'Se enquadra na categoria de atleta MASTER.')

"""– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER"""