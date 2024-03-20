from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) #ceil arrendondando os resultados para cima


import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

import random
num = random.randint(1, 10) #o computador escolhe um numero entre os que estão em parentese
print(num)

import emoji
print(emoji.emojize('Olá mundo :sunglasses:', use_aliases=True))