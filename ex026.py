fr = str(input('Digite uma frase:\n ')).strip().upper()
print(f' A letra A aparece {fr.count("A")} vezes.')
print(f' A primeira letra A apareceu na posição {fr.find("A") + 1}')
print(f' A ultima letra A apareceu por ultimo na posição {fr.rfind("A") + 1}')


