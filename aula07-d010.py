print('CONVERSOR DE MOEDAS')
print()

real=int(input('Digite o valor que deseja converter: R$ '))
conversao_dolar = real / 3.27
print('Com R$ {:.2f} reais você tem U$ {:.2f} dólares '.format(real,conversao_dolar))

