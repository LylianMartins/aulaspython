'''Faça um programa que mostre na tela uma contagem para estouro de fogos de artifício,
indo de 10 até 0, com um pausa de 1 segundo entre eles'''
import emoji
from emoji import emojize
from time import sleep
print('CONTAGEM REGRESSIVA')
for c in range(10,-1, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':fireworks: :fireworks: :fireworks: FOGOS!!!!:fireworks: :fireworks: :fireworks:'))