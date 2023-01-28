s = float(input('Quanto ganha atualmente o funcionario? \nR$ '))
if s <= 1250:
    print(f'Quem ganhava R${s:.2f}, passa agora a ganhar R${s + (s * 15/100):.2f}, por mês.')
else:
    print(f'Quem ganhava R${s:.2f}, passa agora a ganhar R${s + (s * 10/100):.2f}, por mês.')

