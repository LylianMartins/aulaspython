'''Melhore o jogo do DESAFIO 028 onde o co mputador vai pensar em um número
de 0 a 10. Só que agora o jogador vai tentar advinhar até a acertar, mostrando
no final quantos palpites foram necessários para vencer'''

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez')
print('Acertou com {} tentativas!'.format(palpites))