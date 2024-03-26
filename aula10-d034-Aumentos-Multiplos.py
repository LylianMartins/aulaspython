'''Escreva um programa que pergunte a um funcionário o seu salário e calcule o
valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
Para inferiores ou iguais, o aumento é de 15%'''

'''nome = str(input('**** CALCULO DE SALÁRIO ****\nDigite seu nome: '))

sal = float(input('Digite o seu salário atual: R$ '))
if sal >= 1251:
    print = float(input('{}, seu novo salário será de R$ {}'.format(nome,(sal+(sal*10/100) ))))
else:
    print= float(input('{}, seu novo salário será de R$ {}'.format(nome, (sal+(sal*15/100)))))'''

nome = str(input('**** CALCULO DE SALÁRIO ****\nDigite seu nome: '))

sal = float(input('Digite o seu salário atual: R$ '))
if sal >= 1250:
    novo = sal+(sal*10/100)
else:
    novo = sal+(sal*15/100)

print('{}, seu novo salário será de R$ {}'.format(nome, novo))
