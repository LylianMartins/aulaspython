'''Faça um programa que leia um númeo inteiro e diga se ele é ou não
um número primo'''

tot = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[33m', end= '')
        tot += 1
    else:
        print('\33[31m', end='')
    print('{} '.format(c), end='')
print('\n\033O número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print(' E por isso ele é PRIMO!')
else:
    print(' E por isso ele não é PRIMO!')
