'''Escreva um programa que leia a velocidade de uma carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que foi multado,
a multa vai custar R$ 7,00 por cada km acima do limite'''

vel = float(input('*** RADAR ELETRÔNICO *** \n Qual a velocidade: '))
print()
if vel >= 80:
    print('++++++++  ATENÇÃO ++++++++\n    VOCÊ FOI MULTADO!')
    multa = (vel - 80) * 7
    print('Sua multa ficará no valor de R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')