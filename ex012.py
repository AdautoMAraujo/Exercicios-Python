preco = float(input('Digite o preço do produto: R$ '))
des = float(input('Qual é o desconto? '))
print(f'Este produto na liquidação fica por R${preco-( preco * des/100):.2f}')
