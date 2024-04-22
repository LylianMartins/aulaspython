'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie listas extras que vão conter apenas os valores pares ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das tres listas geradas'''

num = list ()
pares = list()
impares = list()
resp = 'SsNn'
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {num}')
print(f'A lista com números pares é {pares}')
print(f'A lista com números impares é {impares}')

