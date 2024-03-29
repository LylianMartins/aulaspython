'''A confederação Nacional de natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- até 9 anos - mirim
- até 14 anos - infantil
- até 19 anos - junior
- até 20 anos - sênior
- acima - master'''


from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc
print('O Atleta tem {} anos'.format(idade))

if idade <= 9:
    print('CATEGORIA MIRIM! ')
elif idade <= 14:
    print('CATEGORIA INFANTIL! ')
elif idade <= 19:
    print('CATEGORIA JUNIOR! ')
elif idade <= 25:
    print('CATEGORIA SÊNIOR! ')
else:
    print('CATEGORIA MASTER! ')