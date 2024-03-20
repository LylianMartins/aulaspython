'''Faça um programa que leia o comprimento de cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa'''

import math
from math import sqrt
print('Comprimento do Cateto')
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hp = math.hypot(co, ca)
print('O cumprimento da hipotenusa é {:.2f}'.format(hp))

'''from math import hypot
from math import sqrt
print('Comprimento do Cateto')
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hp = hypot(co, ca)
print('O cumprimento da hipotenusa é {:.2f}'.format(hp))'''

'''co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O cumprimento da hipotenusa é {:.2f}'.format(hi))'''
