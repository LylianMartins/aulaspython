'''aça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''


valores = []
mai = 0
min = 0
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 0:
        mai = min = valores[cont]
    else:
        if valores[cont] > mai:
            mai = valores[cont]
        if valores[cont] < min:
            min = valores[cont]
print(f'Você digitou {valores}')
print(f'O maior valor digitado foi {mai} na posição ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {min} na posição ', end='')
for i, v in enumerate(valores):
    if v == min:
        print(f'{i}...', end='')
print()

