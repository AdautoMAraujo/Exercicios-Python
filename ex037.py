num = int(input('\033[35mDigite um numero inteiro:\033[35m '))
print('''\033[32mEscolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO.
[ 2 ] Converter para OCTAL.
[ 3 ] Converter para HEXADECIMAL. \033[m''')
opcao = int(input('\033[35mSua opção: \033[m'))
if opcao == 1:
    print(f'{num} Convertido para BINÀRIO é igual a {bin(num)[2:]}.')
elif opcao == 2:
    print(f'{num} Convertido para OCTAL é igual a {oct(num)[2:]}.')
elif opcao == 3:
    print(f'{num} Convertido para HEXADECIMAL é igual a {hex(num)[2:]}.')
else:
    print('\033[31mOpção invalida. Tente novamente!.')
