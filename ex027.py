n = str(input(' Qual é o seu nome?\n ')).strip().split()
print('É um prazer te conhecer!.')
print(f'Seu primeiro nome é {n[0]}.')
print(f'Seu ultimo nome é {n[len(n)-1]}')
