'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo'''

n1 = float(input('+++++ ANALISANDO O TRIÂNGULO +++++\nDigite o 1o segmento: '))
n2 = float(input(('Digite o 2o segmento: ')))
n3 = float(input(('Digite o 3o segmento: ')))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os seguimentos acima PODEM FORMAR um triângulo')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo')
