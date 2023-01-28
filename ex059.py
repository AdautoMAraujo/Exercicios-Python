sair = False
a = int(input('Informe o primeiro um número: '))
b = int(input('Informe o segundo numero: '))
print('''Escolha a opção que deseja:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
while not sair:
    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        somar = a + b
        print(f'A soma entre {a} + {b} é igual a {somar}.')
    if escolha == 2:
        multiplicar = a * b
        print(f'Ao multiplicar {a} X {b}, o resultado é {multiplicar}.')
    if escolha == 3:
        if a < b:
            print(f'O número {b} é o maior!')
        if b < a:
            print(f'O número {a} é o maior!')
        else:
            print('Os dois numeros são iguais.')
    if escolha == 4:
        print('Informe os números novamente.')
        a = int(input('Informe o primeiro um número: '))
        b = int(input('Informe o segundo numero: '))
    if escolha == 5:
        sair = True
    else:
        print('Opção invalida! tente novamente.')
print('Obrigado volte sempre!')

""" Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""