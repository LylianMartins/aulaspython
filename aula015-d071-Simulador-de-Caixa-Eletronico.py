'''Crie um programa que simule o funcionamento de uma caixa eletronico
No inicio, pergunte ao usuario qual sera o valor a ser sacado e o programa
vao informar quantas cedulas de cada valor serão entregues
Considere as cedulas de 50/20/10/1'''

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Qual o valor deseja sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced =10
        elif ced ==10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('{:^30}'.format('TENHA UM BOM DIA!'))