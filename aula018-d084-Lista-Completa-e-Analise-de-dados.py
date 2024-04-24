'''Faça um programa que leia nome e peso de várias pessoas
guardando tudo em uma lista. No final, mostre:
- quantas pessoas foram cadastradas;
uma listagem com as pessoas mais pesadas;
uma listagem com as pessoas mais leves'''

lista = list()
dado = list()
resp = 'SsNn'
peso = 0
mai = 0
men = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(dado) == 0:
        mai = men = lista [1]
    else:
        if lista[1] > mai:
            mai = lista[1]
        if lista[1] < men:
            men = lista [1]
    dado.append(lista[:])
    lista.clear()
    resp = (str(input('Deseja continuar? [S/N] ')))
    if resp in 'Nn':
        break
print('=-'*30)
print(f'Os dados foram {dado}')
print(f'Ao todo, você cadastrou {(len(dado))}.')
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in dado:
    if p[1] == mai:
        print(f'[{p[0]}]')
print()
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for p in dado:
    if p[1] == men:
        print(f'[{p[0]}]')

