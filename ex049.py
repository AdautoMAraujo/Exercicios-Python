from time import sleep
t = int(input('\033[33mDigite um número para ver sua tabuada: \033[m'))
print('-='*5)
for c in range(1, 10+1):
    print(f'{t} X {c} = {t*c}'), sleep(0.3)
print('-='*5)
print('FIM!')
