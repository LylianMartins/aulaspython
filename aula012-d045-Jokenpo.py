'''Crie um programa que faça o computador jogar Jonkenpo com o usuário'''

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print('\33[35;40m+++++JOKENPO+++++\33[m')
print('''Sua opções:
[ 0 ] \33[37mPEDRA\33[m
[ 1 ] PAPEL
[ 2 ] \33[33mTESOURA\33[m''')
jogador = int(input('\33[1mQual é a sua jogada? \33[m'))
print('\33[35;40mJO\33[m')
sleep(1)
print('\33[35:40mKEN\33[m')
sleep(1)
print('\33[35:40mPO!!!\33[m')
print('\33[35m-=\33[m'*13)
print ('O COMPUTADOR jogou {}'.format(itens[computador]))
print('Jogador JOGOU: {}.'.format(itens[jogador]))
print('\33[35m-=\33[m'*13)
if computador == 0:
    if jogador == 0:
        print('\33[:43mEMPATE\33[m')
    elif jogador == 1:
        print('\33[30:42mVOCÊ GANHOU!\33[m')
    elif jogador == 2:
        print('\33[30:41mVOCÊ PERDEU!\33[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('\33[30:41mVOCÊ PERDEU!\33[m')
    elif jogador == 1:
        print('\33[:43mEMPATE\33[m')
    elif jogador == 2:
        print('\33[30:42mVOCÊ GANHOU!\33[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('\33[30:42mVOCÊ GANHOU!\33[m')
    elif jogador == 1:
        print('\33[30:41mVOCÊ PERDEU!\33[m')
    elif jogador == 2:
        print('\33[43mEMPATE\33[m')
    else:
        print('JOGADA INVÁLIDA!')
