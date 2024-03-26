'''Desenvolvaum aprograma que pergunte a distancia de uma viagem em km.
Calcule o preço da passagem, cobrando 0,50 por km para viagens de até 200km
e 0,45 para viagens mais longas'''

km = int(input('****** PREÇO DA PASSAGEM ******\n   Digite a distância da viagem: '))
if km <= 200:
    print('O preço da passagem será de R$ {}'.format(km * 0.50))
else:
    print('O preço da sua passagem será de R$ {}'.format(km * 0.45))


'''km = float(input('****** PREÇO DA PASSAGEM ******\n   Digite a distância da viagem: '))
print('Você está prestes a começar uma viagem de {}km'.format(km))
if km <= 200:
    preço = km * 0.50
else:
    preço = ditância * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preço))'''


