'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu'''

'''s1 = str(input('-----ADVINHE QUAL O NÚMERO-----\nPense em número de 0 a 5\nDigite o número escolhido: '))
from random import choice
n0 = 0
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
lista = (n0, n1, n2, n3, n4, n5)
sorteio = choice(lista)
if s1 == sorteio:
    print('Parabéns, você acertou!!')
else:
    print('Você errou! O número escolhido foi: ', sorteio)'''

from random import randint
from time import sleep
computador = randint(0,5) # faz com que o computador "pense" entre 0 e 5
print('-+-'*20)
print('Vou pensar em número entre 0 e 5. Tente advinhar...')
print('-+-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não {}'.format(computador, jogador))