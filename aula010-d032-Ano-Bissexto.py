'''Faça um programa que leia um ano e mostre se ela é BISSEXTO'''

'''ano = int(input('+++++ É UM ANO BISSEXTO? +++++\n Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é BISSEXTO', ano)
else:
    print('O ano não é BISSEXTO', ano)'''


from datetime import date
ano = int(input('+++++ É UM ANO BISSEXTO? +++++\n Digite um ano, ou coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é BISSEXTO', ano)
else:
    print('O ano não é BISSEXTO', ano)