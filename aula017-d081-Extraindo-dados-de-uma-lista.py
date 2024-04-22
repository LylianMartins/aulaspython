'''Crie um programa que vai ler vários números e colocar em uma
lista, depois disso, mostre:
- quantos numeros fora digitados
- a lista ordenada de forma descrescente
- se o valor 5 foi digitado e está ou não na listq'''

valores = []
resp = 'SsNs'
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja Continuar? [S/N]: ')).strip().upper()
    if resp in 'Nn':
        break
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
n = 5
if n in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')



'''valores = list()
resp = 'SsNs'
cont = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    valores.sort(reverse=True)
    cont += 1
    resp = str(input('Deseja Continuar? [S/N]: ')).strip().upper()
    if resp in 'Nn':
        break
print(f'Você digitou {cont} elementos')
print(f'Os valores em ordem decrescente são {valores}')
n = 5
if n in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')'''
