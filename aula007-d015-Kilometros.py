km = float(input('Quantos KM rodados: '))
dias = int(input('Quantos dias alugados: '))
total = (dias * 60) + (km * 0.15)
print('O preço a pagar da diaria é de {:.2f}'.format(total))