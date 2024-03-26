'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor'''

n1 = int(input('Digite o 1o número: '))
n2 = int(input('Digite o 2o número: '))
n3 = int(input('Digite o 3o número: '))
# verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    menor = n2
if n3 > n1 and n3 > n2:
    menor = n3

print('O maior número é: {}'.format(maior))
print('o menor número é: {}'.format(menor))
