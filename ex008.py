medida = float(input('Uma medida em metros: '))
KM = medida/1000
HM = medida/100
DAM = medida/10
DM = medida*10
CM = medida*100
MM = medida*1000
# print(f'A média de {medida}M em, quilometros equivale a {KM}')
# print(f'A média de {medida}M em, centimetros equivale a {CM}')
print(f'A media de {medida}M.\n Em quilometros é {KM}.\n Em Hectômetro é {HM}.\n Em Decâmetro é {DAM}.\n Em Decímetro é {DM}.\n Em Centímetro é {CM}.\n Em Milímetro é {MM}.')
