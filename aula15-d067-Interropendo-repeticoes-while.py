'''Faça um programa que mostre a tabuada de varios numeros, um de cada vez
para cada valor digitado pelo usuario. o programa será interrompido
quando o número negativo for solicitado'''

from operator import neg
print('GERADOR DE TABUADA')
print()
num = -1
num = neg(num)
while True:
    num = int(input('Tabuada de numero: '))
    if num <= neg(num):
        break
    else:
        for count in range(10):
            print(f'{num} x {count+1} = {num*(count + 1)}')

print('PROGRAMA DE TABUADA ENCERRADO!')
