peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)

if imc <= 18.5:
    print(f'Seu IMC é {imc:.1f} e voçe está, abaixo do peso.')
elif imc <= 25:
    print(f'Seu IMC é {imc:.1f} e voçe está, no peso IDEAL.')
elif imc <= 30:
    print(f'Seu IMC é {imc:.1f} e voçe está, em SOBREPESO.')
elif imc <= 40:
    print(f'Seu IMC é {imc:.1f} e voçe está, com OBESIDADE')
elif imc > 40:
    print(f'Seu IMC é {imc:.1f} e voçe está, com OBESIDADE MORBIDA. Cuidado!')



    """– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida

Aula Anterior
Voltar p"""
