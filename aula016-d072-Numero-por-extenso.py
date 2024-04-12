'''Crie um programa que tenha uma tupla totalmente prenchida com uma contador
por extenso, de zero até 20. Seu programa deverá ler um número pelo teclado (entre zero a 20)
e mostra-lo por extenso'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze','treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Invalido Tente novamente ', end='')
    else:
        print(f'Você digitou o número {numeros[num]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:=^30}'.format(' PROGRAMA FINALIZADO '))



