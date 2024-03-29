'''Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
Equilátero - todos os lados iguais
Isósceles - dois lados iguais
Escaleno - Todos os lados diferentes'''

n1 = float(input('+++++ ANALISANDO O TRIÂNGULO +++++\nDigite o 1o segmento: '))
n2 = float(input(('Digite o 2o segmento: ')))
n3 = float(input(('Digite o 3o segmento: ')))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os seguimentos acima PODEM FORMAR um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo')
