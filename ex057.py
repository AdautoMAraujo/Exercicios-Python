sexo = str(input('Qual seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados invalidos, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
